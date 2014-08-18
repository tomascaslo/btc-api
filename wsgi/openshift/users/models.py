from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	pass

class BusinessOwner(CustomUser):
	is_business_owner = models.BooleanField(default=False)
	conekta_user_token = models.CharField(max_length=30, blank=True)