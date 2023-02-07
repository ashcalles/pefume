from django.db import models
from django.contrib.auth.models import User 

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=50)


class OrderItem(models.Model):
    name = models.CharField(max_length=50)
    
