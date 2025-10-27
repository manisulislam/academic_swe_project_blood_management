from django.contrib.auth.decorators import user_passes_test

def role_required(role_name):
    def decorator(view_func):
        return user_passes_test(lambda u: u.is_authenticated and u.role == role_name)(view_func)
    return decorator
