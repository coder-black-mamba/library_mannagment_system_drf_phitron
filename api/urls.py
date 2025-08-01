from django.urls import path,include
from rest_framework.routers import DefaultRouter

from books.views import BookViewSet , MemberViewSet , AuthorViewSet , CategoryViewSet

router = DefaultRouter()
router.register("books",BookViewSet,basename="books")
router.register("members",MemberViewSet,basename="members")
router.register("authors",AuthorViewSet,basename="authors")
router.register("categories",CategoryViewSet,basename="categories")

urlpatterns = [
    path("",include(router.urls)),
    path("operations/",include("operations.urls")),
]
