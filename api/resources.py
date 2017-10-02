from tastypie.resources import ModelResource
from dreambuy.models import Product
from tastypie.authorization import Authorization, DjangoAuthorization
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from tastypie.authentication import BasicAuthentication
from django.db import IntegrityError
from django.http import JsonResponse


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['email','password','is_active','is_staff','is_superuser']
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()


class Products_list_api(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = "productslistapi"
        authentication = BasicAuthentication()
        # authorization = DjangoAuthorization()



