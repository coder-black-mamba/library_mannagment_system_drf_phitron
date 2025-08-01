from django.urls import path
from .views import borrow_list, return_book
urlpatterns = [
    path("borrow/",borrow_list,name="borrow"),
    path("return/<int:pk>",return_book,name="return"),
]