# views.py

from rest_framework import generics
from .models import BoosUser
from .serializers import AdminSerializer
from drf_yasg.utils import swagger_auto_schema

class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoosUser.objects.all()
    serializer_class = AdminSerializer

    @swagger_auto_schema(
        responses={200: AdminSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(request_body=AdminSerializer)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=AdminSerializer)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema()
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AdminCreateView(generics.CreateAPIView):
    queryset = BoosUser.objects.all()
    serializer_class = AdminSerializer
    @swagger_auto_schema(
        request_body=AdminSerializer,
        operation_summary="Create a new client",
        operation_description="Creates a new client record."
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AdminListView(generics.ListAPIView):
    queryset = BoosUser.objects.all()
    serializer_class = AdminSerializer
