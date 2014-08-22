from django.conf.urls import patterns, include, url

from django.contrib import admin

from tastypie.api import Api
from users.api.user_resource import BusinessOwnerResource

admin.autodiscover()

v1_api = Api(api_name='bitcoindir')
v1_api.register(BusinessOwnerResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls))
)
