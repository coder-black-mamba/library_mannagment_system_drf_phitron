from django.db import models
from books.models import Book
from books.models import Member

# Create your models here.

class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    