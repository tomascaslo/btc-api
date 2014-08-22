from datetime import datetime

from django.db import models

from users.models import BusinessOwner

class CreditCard(models.Model):
	user = models.ForeignKey('users.BusinessOwner')
	conekta_card_token = models.CharField(max_length=30)
	last_four = models.CharField(max_length=4, blank=True)
	name_in_card = models.CharField(max_length=100, blank=True)
	card_type = models.CharField(max_length=50, blank=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return 'Card XXXX-XXXX-XXXX-' + self.last_four + \
				' of user ' + self.user.first_name + \
				' with token ' + self.conekta_card_token

class PaymentTransaction(models.Model):
	credit_card = models.ForeignKey('CreditCard')
	payment_date = models.DateTimeField(default=datetime.now)
	amount = models.DecimalField(decimal_places=8, max_digits=20)
	currency = models.CharField(max_length=10)
	conekta_transaction_id = models.CharField(max_length=30)
	conekta_user_id = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return 'Payment transaction with id: ' + conekta_transaction_id

	class Meta:
		permissions = (
			('view_transaction', 'Can view transaction record.'), 
		)