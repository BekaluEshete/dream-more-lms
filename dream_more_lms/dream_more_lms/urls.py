
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


from users import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LMS API",
        default_version='v1',
        description="API documentation for your Learning Management System",
        contact=openapi.Contact(email="bekelueshete@gmail.com.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('enrollments/', include('enrollments.urls')),
    path('assessments/', include('assessments.urls')),
    path('certificates/', include('certificates.urls')),
    path('notifications/', include('notifications.urls')),
    path('discussions/', include('discussions.urls')),
    path('payments/', include('payments.urls')),
    # for swagger documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    
    path('', views.home),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
