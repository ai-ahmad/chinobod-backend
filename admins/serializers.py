from rest_framework import serializers
from .models import AdminsUser

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminsUser
        fields = "__all__"
