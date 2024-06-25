from django.contrib import admin
from .models import AdminsUser
# Register your models here.


@admin.register(AdminsUser)
class AdminUsers(admin.ModelAdmin):
    list_display = ('phone', 'name','password')
    