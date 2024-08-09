from django.db import models

# Create your models here.
class Mobile(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='mobiles/')

    def __str__(self):
        return self.name

