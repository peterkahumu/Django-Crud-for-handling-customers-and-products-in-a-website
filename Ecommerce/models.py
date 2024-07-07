from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to= 'products/', default="no image uploaded")
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(blank=True, null=True, max_length=100)
    created_when = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

