from django.db import models

# Create your models here.


class Client (models.Model):
    phone = models.CharField(max_length=13)
    password = models.CharField(max_length=300)

    def __str__(self):
        return self.phone
