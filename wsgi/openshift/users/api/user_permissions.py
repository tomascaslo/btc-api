# coding: utf-8

import simplejson

from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized, ImmediateHttpResponse

class BusinessOwnerAuthorization(Authorization):
	"""
	Authorizations for business owners management
	"""
	pass
	# def read_detail(self, object_list, bundle):
	# 	current_user = bundle.request.user
	# 	obj = bundle.obj

	# 	if obj == current_user:
	# 		return True