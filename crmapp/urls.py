from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

import accounts.views
import marketing.views
import contacts.views
import communications.views
import subscribers.views
from accounts.urls import account_urls
from contacts.urls import contact_urls
from communications.urls import comm_urls


urlpatterns = [

    # Marketing pages
    url(r'^$', marketing.views.HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$', subscribers.views.subscriber_new, name='sub_new'),

    # Admin URL
    url(r'^admin/', admin.site.urls),

    # Login/Logout URLs
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'next_page': '/login/'}),

    # Account related URLs
    url(r'^account/new/$', accounts.views.account_cru, name='account_new'),
    url(r'^account/list/$', accounts.views.AccountList.as_view(), name='account_list'),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),

    # Contact related URLS
    url(r'^contact/(?P<pk>[\w-]+)/delete/$', contacts.views.ContactDelete.as_view(), name='contact_delete'),
    url(r'^contact/new/$', contacts.views.contact_cru, name='contact_new'),
    url(r'^contact/(?P<uuid>[\w-]+)/', include(contact_urls)),

    # Communication related URLs
    url(r'^comm/new/$', communications.views.comm_cru, name='comm_new'),
    url(r'^comm/(?P<uuid>[\w-]+)/', include(comm_urls)),
    url(r'^comm/(?P<pk>[\w-]+)/delete/$', communications.views.CommDelete.as_view(), name='comm_delete'),

]