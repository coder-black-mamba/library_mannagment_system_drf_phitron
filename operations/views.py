from rest_framework import viewsets
from .models import Borrow, Book
from .serializers import BorrowSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
# class BorrowViewSet(viewsets.ModelViewSet):
#     queryset = Borrow.objects.all()
#     serializer_class = BorrowSerializer
    
# need to implement functional view

@api_view(['GET','POST'])
def borrow_list(request):
    if request.user.is_authenticated:
        if request.method == 'GET' :
            member_id = request.GET.get('member_id')
            book_id = request.GET.get('book_id')
            if member_id is not None:
                borrow = Borrow.objects.filter(member_id=member_id)
            elif book_id is not None:
                borrow = Borrow.objects.filter(book_id=book_id)
            else:
                borrow = Borrow.objects.all()
            serializer = BorrowSerializer(borrow, many=True)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = BorrowSerializer(data=request.data)
            book = Book.objects.get(pk=request.data['book'])
            if book.available:
                book.available = False
                book.save()
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    return Response({"error": "You are not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['GET', 'POST'])
# def borrow_specific(request,pk):
#     if request.method == 'GET':
#         borrow = Borrow.objects.get(pk=pk)
#         serializer = BorrowSerializer(borrow)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BorrowSerializer(data=request.data)
#         book = Book.objects.get(pk=request.data['book'])
#         if book.available:
#             book.available = False
#             book.save()
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET', 'POST'])
def return_book(request,pk):
    if request.user.is_authenticated:
        if request.method == 'GET' :
            borrow = Borrow.objects.get(pk=pk)
            serializer = BorrowSerializer(borrow)
            return Response(serializer.data)
        if request.method == 'POST':
            serializer = BorrowSerializer(data=request.data)
            book = Book.objects.get(pk=request.data['book'])
            if not book.available:
                book.available = True
                book.save()
                if serializer.is_valid():
                    borrow = Borrow.objects.get(pk=pk)
                    borrow.returned = True
                    borrow.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    return Response({"error": "You are not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Borrow, Book
# from .serializers import BorrowSerializer
# from django.shortcuts import get_object_or_404

# class BorrowListAPIView(APIView):
#     def get(self, request):
#         if request.user.is_authenticated:
#             member_id = request.GET.get('member_id')
#             book_id = request.GET.get('book_id')

#             if member_id is not None:
#                 borrow = Borrow.objects.filter(member_id=member_id)
#             elif book_id is not None:
#                 borrow = Borrow.objects.filter(book_id=book_id)
#             else:
#                 borrow = Borrow.objects.all()

#             serializer = BorrowSerializer(borrow, many=True)
#             return Response(serializer.data)
#         return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

#     def post(self, request):
#         if request.user.is_authenticated:
#             serializer = BorrowSerializer(data=request.data)
#             book = get_object_or_404(Book, pk=request.data['book'])

#             if book.available:
#                 book.available = False
#                 book.save()
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({"error": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)

#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)


# class ReturnBookAPIView(APIView):
#     def get(self, request, pk):
#         if request.user.is_authenticated:
#             borrow = get_object_or_404(Borrow, pk=pk)
#             serializer = BorrowSerializer(borrow)
#             return Response(serializer.data)
#         return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

#     def post(self, request, pk):
#         if request.user.is_authenticated:
#             serializer = BorrowSerializer(data=request.data)
#             book = get_object_or_404(Book, pk=request.data['book'])

#             if not book.available:
#                 book.available = True
#                 book.save()
#                 if serializer.is_valid():
#                     borrow = get_object_or_404(Borrow, pk=pk)
#                     borrow.returned = True
#                     borrow.save()
#                     return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response({"error": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)

#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
