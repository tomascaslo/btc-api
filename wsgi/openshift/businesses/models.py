from django.db import models

from users.models import BusinessOwner
from base.models import Picture 

class BusinessPicture(Picture):
	business = models.ForeignKey('Business')

class BusinessCategory(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

class BusinessLocation(models.Model):
	latitude = models.FloatField()
	longitude = models.FloatField()
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)

	def __str__(self):
		return 'Country: ' + self.country + ', State: ' + self.state + ', City: ' + self.city 

class Business(models.Model):
	user = models.ForeignKey('users.BusinessOwner')
	name = models.CharField(max_length=250)
	real_name = models.CharField(max_length=250, blank=True)
	description = models.TextField()
	logo_url = models.CharField(max_length=200, blank=True)
	website = models.CharField(max_length=200, blank=True)
	has_physical_location = models.BooleanField(default=False)
	phone = models.CharField(max_length=20, blank=True)
	phone2 = models.CharField(max_length=20, blank=True)
	email = models.EmailField(blank=True)
	categories = models.ManyToManyField(BusinessCategory, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

# MUST CHECK WHICH FIELDS CAN BE BLANK OR TRUE