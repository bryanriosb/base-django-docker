# Django
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

# Django Rest Framework
from rest_framework import permissions

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Swagger
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # Django
    path('manager/', admin.site.urls),

    # Apps
    # path('api/v1/', include('apps.common.urls')),
    # path('api/v1/', include(('apps.users.urls', 'users'), namespace='users')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
