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

from ..models import Business
from users.models import BusinessOwner
from base.custom_class import ModelResourceCustom

class BusinessResource(ModelResourceCustom):
	user = fields.ForeignKey(BusinessOwner, 'owner', full=True)

	class Meta:
		queryset = Business.objects.all()
		resource_name = 'business'
		detail_allowed_methods = ['get', 'post', 'patch', 'delete']
		list_allowed_methods = ['get']
		excludes = ['updated_at']
		authorization = Authorization()
		authentication = Authentication()
