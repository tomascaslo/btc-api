from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	pass

class BusinessOwner(CustomUser):
	is_business_owner = models.BooleanField(default=False)
	conekta_user_token = models.CharField(max_length=30, blank=True)

# class CustomUser(AbstractUser):
# 	phone = models.CharField(max_length=20, blank=True)
# 	is_online = models.BooleanField(default=False)

# class BusinessOwner(CustomUser):
# 	last_logout = models.DateTimeField(blank=True, null=True)
# 	is_business_owner = models.BooleanField(default=False)
# 	conekta_user_token = models.CharField(max_length=30, blank=True)