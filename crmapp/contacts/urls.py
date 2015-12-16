from django.conf.urls import url

import views as contacts_views


contact_urls = [
    url(r'^$', contacts_views.contact_detail, name="contact_detail"),
    url(r'^edit/$', contacts_views.contact_cru, name='contact_update'),
]
