# views.py

from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer
from drf_yasg.utils import swagger_auto_schema

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @swagger_auto_schema(
        operation_summary="Retrieve a client",
        operation_description="Retrieves details of a specific client."
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ClientSerializer,
        operation_summary="Update a client",
        operation_description="Updates details of an existing client."
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ClientSerializer,
        operation_summary="Partially update a client",
        operation_description="Partially updates details of an existing client."
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a client",
        operation_description="Deletes an existing client record."
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @swagger_auto_schema(
        request_body=ClientSerializer,
        operation_summary="Create a new client",
        operation_description="Creates a new client record."
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
