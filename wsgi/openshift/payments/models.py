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