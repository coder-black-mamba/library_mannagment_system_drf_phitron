"""
URL configuration for library_mannagment_system project.

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

from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

def test_view(request):
    return HttpResponse("Hello World From /")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", test_view),
    path("api/v1/", include("api.urls")),
]




# schema_view = get_schema_view(
#    openapi.Info(
#       title="Library API",
#       default_version='v1',
#       description="Library API for managing books and members",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@snippets.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
#    authentication_classes=[],
# )

class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_endpoints(self, request):
        # Get all endpoints
        endpoints = super().get_endpoints(request)
        # Filter out anything with 'login' in the path
        endpoints = {k: v for k, v in endpoints.items() if "login" not in k}
        return endpoints

schema_view = get_schema_view(
   openapi.Info(
      title="Library API",
      default_version='v1',
      description="Library API for managing books and members",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=[],
   generator_class=CustomSchemaGenerator,  # << added here
)
urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]
