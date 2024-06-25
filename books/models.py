from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    pdf_url = models.CharField(max_length=300)
    image_url = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    def __str__(self):
        return self.title