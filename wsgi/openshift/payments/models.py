from django.db import models
from users import foodtrucker

# Create your models here.
class Payment(models.Model):
	date_time = models.DateTimeField()
	amount = models.DecimalField()
	conekta_user = models.CharField()
	conekta_card = models.CharField()
	conekta_transaction = models.CharField()
	foodtrucker = models.ForeignKey('foodtrucker')

    def __str__(self):
        return str(self.amount)