from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import contacts.views

from django.conf.urls import *
from tastypie.api import Api
from contacts.api import ContactResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(ContactResource())

urlpatterns = patterns('',
	url(r'^$', contacts.views.ContactListView.as_view(),
		name='contacts-list',
	),
	url(r'^new$', contacts.views.CreateContactView.as_view(),
		name='contacts-new',
	),
	(r'^api/', include(v1_api.urls)),
    # Examples:
    # url(r'^$', 'psmserver.views.home', name='home'),
    # url(r'^psmserver/', include('psmserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
