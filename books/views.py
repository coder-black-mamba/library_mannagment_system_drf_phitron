# external imports
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsLibrarianOrReadOnly, IsLibrarian

# internal imports
from .models import Book, Member, Author, Category
from .serializers import BookSerializer, MemberSerializer, AuthorSerializer, CategorySerializer


# Book Model ViewSet
class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsLibrarianOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsLibrarian]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsLibrarianOrReadOnly]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsLibrarianOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer