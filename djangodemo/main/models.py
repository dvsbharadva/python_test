from django.db import models
from django.db.models.base import Model
from django.db.models.fields import BooleanField, reverse_related


class Contact(models.Model):
    email = models.CharField(max_length=122)
    passwd = models.CharField(max_length=255)
    addr = models.TextField()
    city = models.CharField(max_length=255)
    pincode = models.CharField(max_length=8)
    date = models.DateField(null=True)

    def __str__(self):
        return self.email