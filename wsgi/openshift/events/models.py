from django.db import models
from foodtruck import Foodtruck

class Event(models.Model):
	name = models.CharField(max_length=40)
	date = models.DateField()
	country = models.CharField(max_length=100,blank=True, null=True) #https://developers.google.com/places/documentation/autocomplete
	city = models.CharField(max_length=100,blank=True, null=True) #https://developers.google.com/places/documentation/autocomplete
	place = models.CharField(max_length=100,blank=True, null=True)
	address_line_1 = models.CharField(max_length=300,blank=True, null=True)
	address_line_2 = models.CharField(max_length=300,blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	opening_time = models.DateTimeField(blank=True, null=True)
	closing_time = models.DateTimeField(blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	poster models.URLField(blank=True,null=True)
	CANCELED = 'CN'
	ON = 'ON'
	DELAYED = 'DL'
	POSTPONE = 'PP'
    STATUS_CHOICES = (
        (ON, 'On'),
	    (CANCELED, 'Canceled'),
	    (DELAYED, 'Delayed'),
	    (POSTPONE, 'Postponed'),
    )
    status = models.CharField(max_length=2,
                                      choices=STATUS_CHOICES,
                                      default=ON)
    lineup = models.ManyToManyField(Foodtruck, verbose_name="Lineup",blank=True, null=True)

    def __str__(self):
        return self.name