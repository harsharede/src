from django.conf.urls import url, include
from django.contrib import admin
from . import views

from rest_framework import routers

app_name = "dreambuy"

urlpatterns = [
    #/dreambuy/
    url(r'^$',views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # #/dreambuy/id/
    url(r'^(?P<prdt_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'bid/(?P<prdt_id>\w+)$',views.place_bid, name='place_bid'),
    url(r'^Api_detail/$',views.Api_detail, name='Api_detail'),
    url(r'bid/view_url/',views.form_request_view, name='view_name'),
    url(r'user_bids/',views.user_bids, name='user_bids'),
    url(r'pymnt_success/',views.pymnt_success, name='pymntsuccess'),
    # url(r'pymnt/(?P<slug>[a-zA-Z0-9_.-]+)/$', views.pymnt, name='pymnt'),
    url(r'pymnt/(?P<slug>\w+)$', views.pymnt, name='pymnt'),
    url (r'FAQs/$',views.FAQs)
]



