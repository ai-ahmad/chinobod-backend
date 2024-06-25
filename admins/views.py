from django.shortcuts import render

from rest_framework import generics
from .models import AdminsUser
from .serializers import AdminSerializer

class AdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdminsUser.objects.all()
    serializer_class = AdminSerializer

class AdminCreateView(generics.CreateAPIView):
    queryset = AdminsUser.objects.all()
    serializer_class = AdminSerializer()