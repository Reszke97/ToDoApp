from rest_framework import serializers
from . models import *
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.exceptions import TokenBackendError
from django.utils.translation import gettext as _

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    #password = serializers.CharField(min_length=8, write_only=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ('email', 'user_name', 'password')
        # extra_kwargs = {'password': {'write_only': True}}
        extra_kwargs = {
            'email': {'write_only': True, 'required': True},
            'user_name': {'write_only': True, 'required': True},
            'password': {'write_only': True, 'required': True},
        }
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance

class AddToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('description', 'deadline', 'title', 'user_id', 'id', 'isDone')
