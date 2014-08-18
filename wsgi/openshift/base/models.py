from django.db import models

# Create your models here.
class Picture(models.Model):
	name = models.CharField(max_length=100, blank=True)
	picture_url = models.CharField(max_length=200)

	def __str__(self):
		return self.picture_url