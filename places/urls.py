from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
    
    # API endpoints
    path('api/search/', views.search_places, name='search_places'),
    path('api/hidden-places/', views.hidden_places_api, name='hidden_places'),
    path('api/coimbatore-places/', views.coimbatore_places_api, name='coimbatore_places'),
    path('api/trichy-places/', views.trichy_places_api, name='trichy_places'),
    path('api/chennai-places/', views.chennai_places_api, name='chennai_places'),
    path('api/madurai-places/', views.madurai_places_api, name='madurai_places'),
]
