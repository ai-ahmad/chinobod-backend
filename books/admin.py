from django.contrib import admin
from .models import Books
# Register your models here.


@admin.register(Books)
class Books(admin.ModelAdmin):
    list_display = ('title', 'author', 'pdf_url', 'image_url', 'type')