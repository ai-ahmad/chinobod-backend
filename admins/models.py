from django.db import models

class AdminsUser(models.Model):
    TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('secretar', 'Secretar'),
    ]

    phone = models.CharField(max_length=13)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=300)
    type = models.CharField(max_length=200, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
