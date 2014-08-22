from django.db import models

from businesses.models import Business
from base.models import Picture

class ProductPicture(Picture):
	product = models.ForeignKey('Product')

class Product(models.Model):
	business = models.ForeignKey('businesses.Business')
	
	name = models.CharField(max_length=150)
	price = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
	price_in_bitcoin = models.DecimalField(max_digits=20, decimal_places=8, blank=True, null=True)
	discount = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

