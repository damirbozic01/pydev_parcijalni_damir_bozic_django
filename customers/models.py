from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=150)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def str(self):
        return self.name
    