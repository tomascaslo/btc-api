import simplejson
import time

from guardian.shortcuts import get_perms, assign_perm

from tastypie import fields
from tastypie.exceptions import NotFound
from tastypie.utils import trailing_slash
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication, SessionAuthentication
from tastypie.http import HttpAccepted, HttpNotFound, HttpBadRequest,\
	HttpUnauthorized

from ..models import PaymentTransaction, CreditCard
from businesses.models import Business
from users.models import BusinessOwner
from base.custom_class import ModelResourceCustom

class PaymentTransactionResource(ModelResourceCustom):
	credit_card = field.ForeignKey(CreditCard, 'credit_card')

	class Meta:
		queryset = PaymentTransaction.objects.all()
		resource_name = 'payment_transaction'
		list_allowed_methods = ['get']
		excludes = ['created_at', 'updated_at']
		authorization = Authorization()
		authentication = Authentication()

class CreditCardResource(ModelResourceCustom):
	business_owner = fields.ForeignKey(BusinessOwner, 'owner')

	class Meta:
		queryset = CreditCard.objects.all()
		resource_name = 'credit_card'
		detail_allowed_methods = ['post', 'delete']
		list_allowed_methods = ['get']
		authorization = Authorization()
		authentication = Authentication()
