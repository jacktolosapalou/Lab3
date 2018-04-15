from django.db import models

# Create your models here.


class User(models.Model):
	email = models.CharField(primary_key=True)
	firstName = models.CharField()
	lastName = models.CharField()
	address = models.CharField()


class Cart(models.Model):
	cartCode = models.IntegerField()
	cartPrice = models.FloatField()
	cartPaid = models.NullBooleanField()


class Product(models.Model):
	productPrice = models.FloatField()
	productName = models.CharField()
	productDesc = models.CharField()