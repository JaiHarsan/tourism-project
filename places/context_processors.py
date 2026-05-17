from .models import User


def user_context(request):
    """
    Custom context processor to add MongoDB user to template context.
    This ensures proper authentication checks in templates.
    """
    context = {}
    
    # Check if user_id is in session (custom authentication)
    if 'user_id' in request.session:
        try:
            user = User.objects.get(id=request.session['user_id'])
            context['user'] = user
            # Add is_authenticated property for template checks
            context['user'].is_authenticated = True
        except User.DoesNotExist:
            # User doesn't exist but session points to them - clear session
            request.session.flush()
            context['user'] = None
    else:
        context['user'] = None
    
    return context
