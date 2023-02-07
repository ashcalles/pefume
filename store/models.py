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
    
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class ShippingAddress(models.Model):
    #customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	#order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    customer = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    date_added = models.CharField(max_length=50)

    def __str__(self):
        return self.address