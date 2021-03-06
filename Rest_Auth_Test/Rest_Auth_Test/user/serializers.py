from .models import User
from rest_framework import serializers
from django.contrib.auth.models import Group
from django import forms


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    groups = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name")

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'groups',)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
