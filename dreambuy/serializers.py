from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ( 'username', 'password')




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProdctsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fileds = ('Product_name','Product_id')