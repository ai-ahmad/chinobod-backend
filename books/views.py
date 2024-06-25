from django.shortcuts import render

from rest_framework import generics
from .models import Books
from .serializer import BooksSerializer

class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksCreateView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer()


class BookListView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer()