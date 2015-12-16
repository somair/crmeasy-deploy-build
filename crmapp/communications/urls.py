from django.conf.urls import url

import views as communications_views


comm_urls = [
    url(r'^$', communications_views.comm_detail, name="comm_detail"),
    url(r'^edit/$', communications_views.comm_cru, name='comm_update'),
]
