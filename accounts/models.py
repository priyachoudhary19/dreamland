from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()   #unlimited data


class registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.name