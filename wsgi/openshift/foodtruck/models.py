from django.db import models

class Foodtruck(models.Model):
	name = models.CharField(max_length=40)
	logo = models.ImageField()
	picture = models.ImageField()
	foodtype = models.ManyToManyField(Foodtype, verbose_name="foodtype list")
	phone = models.IntegerField()
	facebook = models.URLField()
	twitter = models.URLField()
	tumblr = models.URLField()
	instagram = models.URLField()
	webpage = models.URLField()
	preorder_link = models.URLField()
	menu = models.ManyToManyField(MenuItem, verbose_name="complete menu")

	def __str__(self):
        return self.name

class Foodtype(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
        return self.name

class MenuItem(models.Model):
	name = models.CharField(max_length=40)
	description = models.TextField()
	price = models.DecimalField()

	def __str__(self):
        return self.name

class Association(models.Model):
	name = models.CharField(max_length=100)
	country = CountryField() #https://developers.google.com/places/documentation/autocomplete
	city = models.CharField() #https://developers.google.com/places/documentation/autocomplete
	logo = models.ImageField()
	verify = models.BooleanField(default=False)
	passcode = models.CharField(max_length=40)

	def __str__(self):
        return self.name