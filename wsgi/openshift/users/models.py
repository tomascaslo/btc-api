from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	phone = models.CharField(max_length=20, blank=True)
	is_online = models.BooleanField(default=False)
	last_logout = models.DateTimeField(blank=True, null=True)

	def set_permissions(self, permissions, update=False):
		if update:
			pass

class BusinessOwner(CustomUser):
	conekta_user_token = models.CharField(max_length=30, blank=True)
	is_business_owner = models.BooleanField(default=False)