from django.db import models

from products.models import Referral

class Referral(models.Model):
	product = models.ForeignKey('products.Referral')
	url = models.CharField(max_length=200)
	real_url = models.CharField(max_length=200)
	number_of_hits = models.IntegerField(default=0)

	def __str__(self):
		return self.url

	def add_hit(self):
		self.number_of_hits += 1