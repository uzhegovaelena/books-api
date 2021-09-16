from .models import Book
from rest_framework import viewsets, permissions
from .serializer import BooksSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = BooksSerializer
