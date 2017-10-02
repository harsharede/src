"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from dreambuy import views
from rest_framework.urlpatterns import format_suffix_patterns
from api.resources import Products_list_api,UserResource
import re
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(Products_list_api())
# v1_api.register(CreateUserResource())
# products_list_api = Products_list_api()

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
# router.register(r'Products_listapi', views.ProductViewSet)

app_name = 'dreambuy'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^dreambuy/', include('dreambuy.urls', namespace='dreambuy', app_name='dreambuy')),
    url(r'^', include('dreambuy.urls', namespace='dreambuy', app_name='dreambuy')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^api_productslist/',views.get_Product_list),
    url(r'^api_reg/$',views.CreateAPIView.as_view(),name='user'),
    # url (r'^Products_listapi/$',views.ProductViewSet,name='ProductViewSet')
    url(r'pymnt/$', views.pymnt, name='pymnt'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^register/$', views.register, name='register'),
    url (r'FAQs/$',views.FAQs)
]

