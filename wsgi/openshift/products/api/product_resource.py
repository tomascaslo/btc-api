import simplejson
import time

from guardian.shortcuts import get_perms

from tastypie import fields
from tastypie.exceptions import NotFound
from tastypie.utils import trailing_slash
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication, SessionAuthentication
from tastypie.http import HttpAccepted, HttpNotFound, HttpBadRequest,\
	HttpUnauthorized

from ..models import Product
from businesses.models import Business
from users.models import BusinessOwner
from base.custom_class import ModelResourceCustom

class ProductResource(ModelResourceCustom):
	business = fields.ForeignKey(Business, 'business')

	class Meta:
		queryset = Product.objects.all()
		resource_name = 'product'
		detail_allowed_methods = ['get', 'post', 'patch', 'delete']
		list_allowed_methods = ['get', 'post']
		excludes = ['created_at', 'updated_at']
		authorization = Authorization()
		authentication = Authentication()
