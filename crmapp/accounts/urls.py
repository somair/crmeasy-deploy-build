from django.conf.urls import url

import views as accounts_views


account_urls = [
    url(r'^$', accounts_views.account_detail, name='account_detail'),
    url(r'^edit/$', accounts_views.account_cru, name='account_update'),
]
