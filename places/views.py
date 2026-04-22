from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mongoengine import Q
from datetime import datetime


try:
    from .models import Place, User
    from .serializers import PlaceSerializer
except ImportError:
    Place = None
    User = None
    PlaceSerializer = None



def home(request):
    """Home view - places are loaded dynamically via API"""
    
    return render(request, 'base.html')



def login_view(request):
    """Handle user login with MongoDB User model"""
    # Check if already logged in
    if 'user_id' in request.session:
        return redirect('places:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                # Store user in session
                request.session['user_id'] = str(user.id)
                request.session['username'] = user.username
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('places:home')
            else:
                messages.error(request, "Invalid username or password")
        except User.DoesNotExist:
            messages.error(request, "Invalid username or password")

    return render(request, 'auth/login.html')



def signup_view(request):
    """Handle user registration with MongoDB User model"""
    # Check if already logged in
    if 'user_id' in request.session:
        return redirect('places:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'auth/signup.html')

        # Check if username already exists
        if User.objects(username=username):
            messages.error(request, "Username already exists")
            return render(request, 'auth/signup.html')
        
        # Check if email already exists
        if User.objects(email=email):
            messages.error(request, "Email already exists")
            return render(request, 'auth/signup.html')

        try:
            # Create new user in MongoDB
            user = User(
                username=username,
                email=email
            )
            user.set_password(password)
            user.save()
            
            # Store user in session
            request.session['user_id'] = str(user.id)
            request.session['username'] = user.username
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('places:home')
        except Exception as e:
            messages.error(request, f"Error creating account: {str(e)}")
            return render(request, 'auth/signup.html')

    return render(request, 'auth/signup.html')



def logout_view(request):
    """Handle user logout - completely clear session"""
    username = request.session.get('username', 'User')
    
    # Completely flush the session - removes all session data
    request.session.flush()
    
    messages.success(request, f"Goodbye, {username}! You have been logged out.")
    return redirect('places:home')



def profile_view(request):
    """Display user profile"""
    if 'user_id' not in request.session:
        return redirect('places:login')
    
    try:
        user = User.objects.get(id=request.session['user_id'])
        return render(request, 'auth/profile.html', {'user': user})
    except User.DoesNotExist:
        return redirect('places:login')



def edit_profile_view(request):
    """Edit user profile"""
    if 'user_id' not in request.session:
        return redirect('places:login')
    
    try:
        user = User.objects.get(id=request.session['user_id'])
    except User.DoesNotExist:
        return redirect('places:login')
    
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', user.email)
        user.updated_at = datetime.now().isoformat()
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('places:profile')

    return render(request, 'auth/edit_profile.html', {'user': user})



@api_view(['GET'])
def search_places(request):
    """API endpoint to search and filter places (MongoDB)"""
    query = request.GET.get('q', '').lower()
    category = request.GET.get('category', 'all')
    
    if not Place:
        return Response({'results': []})
    
    # Build MongoEngine query
    if category != 'all':
        places = Place.objects.filter(category=category)
    else:
        places = Place.objects.all()
    
    if query:
        places = places.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(city__icontains=query)
        )
    
    # Convert to list of dicts
    results = [place.to_dict() for place in places]
    return Response({'results': results})



@api_view(['GET'])
def hidden_places_api(request):
    """
    API endpoint for hidden and less-explored places (MongoDB)
    Query parameters:
    - category: Filter by category (hidden_spots, falls, temple, food, or 'all')
    - search: Search query for place name, description, or location
    - city: Filter by city (defaults to Pollachi)
    """
    if not Place:
        return Response({
            'count': 0,
            'places': [],
            'categories': {}
        })
    
    # Get query parameters
    category_filter = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '').lower()
    city_filter = request.GET.get('city', 'pollachi')
    
    # Build MongoEngine query
    places = Place.objects.filter(city=city_filter)
    
    # Filter by category if specified
    if category_filter != 'all':
        places = places.filter(category=category_filter)
    
    # Filter by search query
    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    # Convert to list of dicts
    places_data = [place.to_dict() for place in places]
    
    # Get category breakdown
    category_counts = {
        'hidden_spots': Place.objects.filter(city=city_filter, category='hidden_spots').count(),
        'falls': Place.objects.filter(city=city_filter, category='falls').count(),
        'temple': Place.objects.filter(city=city_filter, category='temple').count(),
        'food': Place.objects.filter(city=city_filter, category='food').count(),
    }
    
    return Response({
        'count': len(places_data),
        'city': city_filter,
        'places': places_data,
        'categories': category_counts
    })


# ================= API: COIMBATORE PLACES =================
@api_view(['GET'])
def coimbatore_places_api(request):
    """
    API endpoint for Coimbatore hidden and less-explored places (MongoDB)
    Query parameters:
    - category: Filter by category (hidden_spots, falls, temple, food, or 'all')
    - search: Search query for place name, description, or location
    """
    if not Place:
        return Response({
            'count': 0,
            'places': [],
            'categories': {}
        })
    
    # Get query parameters
    category_filter = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '').lower()
    
    # Build MongoEngine query
    places = Place.objects.filter(city='coimbatore')
    
    if category_filter != 'all':
        places = places.filter(category=category_filter)
    
    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    places_data = [place.to_dict() for place in places]
    
    # Get category breakdown for Coimbatore
    category_counts = {
        'hidden_spots': Place.objects.filter(city='coimbatore', category='hidden_spots').count(),
        'falls': Place.objects.filter(city='coimbatore', category='falls').count(),
        'temple': Place.objects.filter(city='coimbatore', category='temple').count(),
        'food': Place.objects.filter(city='coimbatore', category='food').count(),
    }
    
    return Response({
        'count': len(places_data),
        'city': 'coimbatore',
        'places': places_data,
        'categories': category_counts
    })


# ================= API: TRICHY PLACES =================
@api_view(['GET'])
def trichy_places_api(request):
    """
    API endpoint for Trichy hidden and less-explored places (MongoDB)
    Query parameters:
    - category: Filter by category (hidden_spots, falls, temple, food, or 'all')
    - search: Search query for place name, description, or location
    """
    if not Place:
        return Response({
            'count': 0,
            'places': [],
            'categories': {}
        })
    
    # Get query parameters
    category_filter = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '').lower()
    
    # Build MongoEngine query
    places = Place.objects.filter(city='trichy')
    
    if category_filter != 'all':
        places = places.filter(category=category_filter)
    
    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    places_data = [place.to_dict() for place in places]
    
    # Get category breakdown for Trichy
    category_counts = {
        'hidden_spots': Place.objects.filter(city='trichy', category='hidden_spots').count(),
        'falls': Place.objects.filter(city='trichy', category='falls').count(),
        'temple': Place.objects.filter(city='trichy', category='temple').count(),
        'food': Place.objects.filter(city='trichy', category='food').count(),
    }
    
    return Response({
        'count': len(places_data),
        'city': 'trichy',
        'places': places_data,
        'categories': category_counts
    })


# ================= API: CHENNAI PLACES =================
@api_view(['GET'])
def chennai_places_api(request):
    """
    API endpoint for Chennai hidden and less-explored places (MongoDB)
    Query parameters:
    - category: Filter by category (hidden_spots, falls, temple, food, or 'all')
    - search: Search query for place name, description, or location
    """
    if not Place:
        return Response({
            'count': 0,
            'places': [],
            'categories': {}
        })
    
    # Get query parameters
    category_filter = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '').lower()
    
    # Build MongoEngine query
    places = Place.objects.filter(city='chennai')
    
    if category_filter != 'all':
        places = places.filter(category=category_filter)
    
    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    places_data = [place.to_dict() for place in places]
    
    # Get category breakdown for Chennai
    category_counts = {
        'hidden_spots': Place.objects.filter(city='chennai', category='hidden_spots').count(),
        'falls': Place.objects.filter(city='chennai', category='falls').count(),
        'temple': Place.objects.filter(city='chennai', category='temple').count(),
        'food': Place.objects.filter(city='chennai', category='food').count(),
    }
    
    return Response({
        'count': len(places_data),
        'city': 'chennai',
        'places': places_data,
        'categories': category_counts
    })


# ================= API: MADURAI PLACES =================
@api_view(['GET'])
def madurai_places_api(request):
    """
    API endpoint for Madurai hidden and less-explored places (MongoDB)
    Query parameters:
    - category: Filter by category (hidden_spots, falls, temple, food, or 'all')
    - search: Search query for place name, description, or location
    """
    if not Place:
        return Response({
            'count': 0,
            'places': [],
            'categories': {}
        })
    
    # Get query parameters
    category_filter = request.GET.get('category', 'all')
    search_query = request.GET.get('search', '').lower()
    
    # Build MongoEngine query
    places = Place.objects.filter(city='madurai')
    
    if category_filter != 'all':
        places = places.filter(category=category_filter)
    
    if search_query:
        places = places.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    
    places_data = [place.to_dict() for place in places]
    
    # Get category breakdown for Madurai
    category_counts = {
        'hidden_spots': Place.objects.filter(city='madurai', category='hidden_spots').count(),
        'falls': Place.objects.filter(city='madurai', category='falls').count(),
        'temple': Place.objects.filter(city='madurai', category='temple').count(),
        'food': Place.objects.filter(city='madurai', category='food').count(),
    }
    
    return Response({
        'count': len(places_data),
        'city': 'madurai',
        'places': places_data,
        'categories': category_counts
    })