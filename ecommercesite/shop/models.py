from django.db import models

class Products(models.Model):

    def __str__(self):
        return self.name 

    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

class Order(models.Model):
    items =  models.CharField(max_length=1000)
    fullname =  models.CharField(max_length=200)
    email =  models.CharField(max_length=200)
    address =  models.CharField(max_length=1000)
    city =  models.CharField(max_length=200)
    province =  models.CharField(max_length=200)
    zipcode =  models.CharField(max_length=200)
    total = models.FloatField()
