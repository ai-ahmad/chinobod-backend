from django.contrib import admin
from .models import BoosUser
# Register your models here.


@admin.register(BoosUser)
class BoosUser(admin.ModelAdmin):
    list_display = ('phone', 'type', 'name','password')
    