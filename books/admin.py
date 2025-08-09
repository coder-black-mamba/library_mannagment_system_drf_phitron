from django.contrib import admin
from .models import Book,Member,Author,Category
# Register your models here.
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Author)
admin.site.register(Category)
