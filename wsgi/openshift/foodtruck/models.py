from django.db import models

class Foodtype(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Foodtruck(models.Model):
	name = models.CharField(max_length=100)
	logo = models.URLField(blank=True, null=True)
	picture = models.URLField(blank=True, null=True)
	foodtype = models.ManyToManyField(Foodtype, verbose_name="foodtype list",blank=True, null=True)
	phone = models.IntegerField(blank=True, null=True)
	# eat24, semeantoja, atumesa, etc
	preorder_link = models.URLField(blank=True, null=True)
	association = models.ForeignKey('Association',blank=True, null=True)
	country = models.CharField(max_length=100) #https://developers.google.com/places/documentation/autocomplete
	city = models.CharField(max_length=100) #https://developers.google.com/places/documentation/autocomplete

	def __str__(self):
		return self.name

class Location(models.Model):
	foodtruck = models.ForeignKey('Foodtruck')
	latitude = models.FloatField()
	longitude = models.FloatField()
	date = models.DateField()
	opening_time = models.DateTimeField(blank=True, null=True)
	closing_time = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return str(self.latitude) + ',' + str(self.longitude)

class SocialMedia(models.Model):
	TWITTER = 'TW'
	FACEBOOK = 'FB'
	TUMBLR = 'TB'
	INSTAGRAM = 'IN'
	PINTEREST = 'PN'
	YOUTUBE = 'YT'
	WEB = 'WB'
	MEDIUM = 'MD'
	VINE = 'VN'
	FOURSQUARE = 'FQ'
	SITE_CHOICES = (
		(FACEBOOK, 'Facebook'),
		(TWITTER, 'Twitter'),
		(TUMBLR, 'Tumblr'),
		(INSTAGRAM, 'Instagram'),
		(PINTEREST, 'Pinterest'),
		(YOUTUBE, 'Youtube'),
		(WEB, 'Web Page'),
		(MEDIUM, 'Medium'),
		(VINE, 'Vine'),
		(FOURSQUARE, 'Foursquare')
	)
	site = models.CharField(max_length=2,
							choices=SITE_CHOICES,
							default=FACEBOOK)
	url = models.URLField()
	foodtruck = models.ForeignKey('Foodtruck')

	def __str__(self):
		return self.url

class MenuItem(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)
	picture = models.URLField(blank=True, null=True)
	foodtruck = models.ForeignKey('Foodtruck')

	def __str__(self):
		return self.name

class Association(models.Model):
	name = models.CharField(max_length=100)
	country = models.CharField(max_length=100) #https://developers.google.com/places/documentation/autocomplete
	city = models.CharField(max_length=100) #https://developers.google.com/places/documentation/autocomplete
	logo = models.URLField(blank=True, null=True)
	verified = models.BooleanField(default=False)
	passcode = models.CharField(max_length=40,blank=True, null=True)

	def __str__(self):
		return self.name