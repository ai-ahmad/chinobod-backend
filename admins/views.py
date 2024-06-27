from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from .models import AdminsUser
from .serializers import AdminSerializer

class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdminsUser.objects.all()
    serializer_class = AdminSerializer

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
    queryset = AdminsUser.objects.all()
    serializer_class = AdminSerializer
