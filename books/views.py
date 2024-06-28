# views.py

from rest_framework import generics
from .models import Books
from .serializer import BooksSerializer
from drf_yasg.utils import swagger_auto_schema

class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    @swagger_auto_schema(
        responses={200: BooksSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=BooksSerializer)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=BooksSerializer)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema()
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BooksCreateView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookListView(generics.ListAPIView):
    @swagger_auto_schema(
        request_body=ClientSerializer,
        operation_summary="Get",
        operation_description="get"
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
