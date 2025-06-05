# Import necessary modules
from django.contrib import admin  # Django admin module
from django.urls import path       # URL routing
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import login_page, register_page  # Import views

# Define URL patterns
urlpatterns = [

    path('login/', login_page, name='login_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
    # Add 'home' path only if you have a home view defined
    # path('home/', home, name="home"),  # Uncomment and fix import if needed
]

# Serve media files if DEBUG is True (development mode)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()