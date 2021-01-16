from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Associates(models.Model):
    name = models.CharField(max_length=30 , null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30 , null=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('indoor','Indoor'),
        ('outdoor','Outdoor'),
        
    )
    name = models.CharField(max_length=30 , null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=30 , null=True,choices=CATEGORY,blank=True)
    description = models.CharField(max_length=300 , null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS = (
        ('pending','Pending'),
        ('Out For delivery','Out For Delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Associates,null=True,on_delete = models.SET_NULL)
    products = models.ForeignKey(Product,null=True,on_delete = models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(choices=STATUS,max_length=200,null=True)
    note = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.products.name
