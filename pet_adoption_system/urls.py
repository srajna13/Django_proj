"""
URL configuration for pet_adoption_system project. 

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from adoption.views import home_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Pet Adoption API",
        default_version='v1',
        description="API documentation for the Pet Adoption System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@petadoption.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', home_view, name="home"),
    path('admin/', admin.site.urls),
    path('api/', include('adoption.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Include your app's URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),  # Fix here
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
]

# from rest_framework.schemas import get_schema_view
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi
# from django.urls import path

# schema_view = get_schema_view(
#     openapi.Info(title="Pet Adoption API", default_version='v1'),
#     public=True,
# )

# urlpatterns += [
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
# ]
