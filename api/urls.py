from django.http import HttpResponse
from django.urls import path
from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

def hello_world(request):
    return HttpResponse("Hello World from api/v1/")


urlpatterns = [
    path('', hello_world),
]
