from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=100)
    def __str__(self):
        return self.category
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
