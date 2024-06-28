from rest_framework import serializers
from .models import BoosUser

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoosUser
        fields = "__all__"
