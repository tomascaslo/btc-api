import simplejson
import time

from guardian.shortcuts import get_perms

from tastypie import fields
from tastypie.exceptions import NotFound
from tastypie.utils import trailing_slash
from tastypie.authorization import Authorization
from tastypie.authentication import SessionAuthentication
from tastypie.http import HttpAccepted, HttpNotFound, HttpBadRequest,\
	HttpUnauthorized

from django.db.models import Q
from django.conf import settings
from django.conf.urls import url
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.forms import AuthenticationForm

from ..models import BusinessOwner
from .user_permissions import BusinessOwnerAuthorization
from base.custom_class import ModelResourceCustom


class BusinessOwnerResource(ModelResourceCustom):
	"""
	Resource for management of BusinessOwner
	"""

	class Meta:
		resource_name = 'business_owner'
		queryset = BusinessOwner.objects.all()
		detail_allowed_methods = ['get', 'post', 'patch']
		list_allowed_methods = ['get']
		excludes = ['last_name', 'is_staff', 'is_superuser', 'password', 'is_active',
					'conekta_user_token']
		fields_to_save = ['phone', 'password', 'password2', 'first_name', 'email',
						'username', 'permissions']
		fields_to_patch = ['phone', 'password', 'password2', 'first_name', 'permissions']
		authentication = SessionAuthentication()
		authorization = BusinessOwnerAuthorization()

	def obj_create(self, bundle, **kwargs):
		# Clean elements not desired for saving
		for key in bundle.data.keys():
			if key not in self._meta.fields_to_save:
				bundle.data.pop(key)

		permissions = bundle.data.get('permissions', [])
		bundle = super(BusinessOwnerResource, self).obj_create(bundle, **kwargs)

		# Establish permissions
		bundle.obj = bundle.obj.set_permissions(permissions)

		# Generate encrypted password
		bundle.obj.set_password(bundle.data.get('password'))
		bundle.obj.save()

		return bundle

	def obj_update(self, bundle, skip_errors=False, **kwargs):
		# Clean elements not desired for updating
		for key in bundle.data.keys():
			if key not in self._meta.fields_to_patch:
				bundle.data.pop(key)

		password = bundle.data.get('password', False)

		permissions = bundle.data.get('permissions', [])

		bundle = super(BusinessOwnerResource, self).obj_create(
			bundle, skip_errors=False, **kwargs)

		bundle.obj = bundle.obj.set_permissions(permissions, update=True)

		if password and \
			bundle.request.user.password != password:
			bundle.obj.set_password(password)
			bundle.obj.save()

		return bundle

	def prepend_urls(self):
		return [
			url(
				r"^(?P<resource_name>%s)/login%s$"
				% (
					self._meta.resource_name,
					trailing_slash()
				),
				self.wrap_view('login'), name="api_login"
			),
			url(
				r"^(?P<resource_name>%s)/logout%s$"
				% (
					self._meta.resource_name,
					trailing_slash()
				),
				self.wrap_view('logout'), name="api_logout"
			),
		]

	def login(self, request, **kwargs):
		self.method_check(request, allowed=['post'])
		data = simplejson.loads(request.body)

		username = data.get('username', '')
		password = data.get('password', '')

		user = None
		logged_in = False

		try: 
			form = AuthenticationForm(data={
				'username': username, 'password': password
				})
			if form.is_valid():
				user = form.get_user()
				if user:
					auth_login(request, user)
		except BusinessOwner.DoesNotExist as e:
			print e

		if logged_in and user:
			try:
				current_user = BusinessOwner.objects.get(pk=user.id)
				current_user.is_online = True
				current_user.save()
			except BusinessOwner.DoesNotExist as e:
				print e

			bundle = self.build_bundle(obj=user, request=request)

			desired_format = self.determine_format(request)

			data = self.serialize(
				request, self.full_dehydrate(bundle), desired_format)
			response = {"user": self.full_dehydrate(bundle)}

			return self.create_response(request, response)
		else:
			return HttpBadRequest()

	def logout(self, request, **kwargs):
		self.method_check(request, allowed=['post'])
		try:
			try:
				current_user = BusinessOwner.objects.get(pk=request.user.id)
				current_user.last_logout = datetime.now()
				current_user.is_online = False
				current_user.save()
			except BusinessOwner.DoesNotExist as e:
				print e

			logout(request)
			return HttpAccepted()
		except:
			return HttpBadRequest()