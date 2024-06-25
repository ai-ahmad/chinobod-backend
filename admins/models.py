from django.db import models


class AdminsUser(models.Model):
    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=300)
    def __str__(self):
        return self.name
