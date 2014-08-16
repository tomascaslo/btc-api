from django.db import models
from users.models import Foodtrucker

# Create your models here.
class Payment(models.Model):
	date_time = models.DateTimeField()
	amount = models.DecimalField(decimal_places=2, max_digits=6)
	conekta_user = models.CharField(max_length=30)
	conekta_card = models.CharField(max_length=30)
	conekta_transaction = models.CharField(max_length=30)
	foodtrucker = models.ForeignKey('users.Foodtrucker')

	def __str__(self):
		return str(self.amount)