from re import search
from django.db import models
from django.db.models import query
from django.db.models.expressions import Value
from django.utils.six import reraise
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import profile


User = get_user_model()


class signupserializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=15)
    first_name = serializers.CharField(max_length=15)
    last_name = serializers.CharField(max_length=15)
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        profile.objects.create(user = user , first_name = first_name , last_name = last_name)
        return user


class Loginserailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["phone","password"]

class profileserializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = "__all__"

class changepasswordserailzer(serializers.Serializer):
    new_password = serializers.CharField(max_length=25)
    retype_password = serializers.CharField(max_length=25)
    user = serializers.CharField(max_length = 3)

    def create(self, validated_data):
        query = User.objects.all()
        new_password = validated_data.get("new_password")
        retype_password = validated_data.get("retype_password")
        user_id = validated_data.get("user")
        if new_password != retype_password:
            raise ValueError("password's didn't match !!")
        else:
            user = get_object_or_404(query , pk=user_id)
            print(user)
            user.set_password(new_password)
            user.save()
            return user

class GetUserserailizer(serializers.ModelSerializer):
    Profile = profileserializer(read_only = True)

    class Meta:
        model = User
        fields = [
            "id",
            "password",
            "last_login",
            "is_admin",
            "phone",
            "email",
            "is_staff",
            "is_active",
            "created_date",
            "Profile",
        ]
        extra_kwargs = {"password": {"write_only": True}}
        read_only_fields = [
            "id",
            "last_login",
            "date_joined",
        ]

    def create(self, validated_data):
        user =  super(GetUserserailizer).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

class Userupdateserailizer(serializers.ModelSerializer):
    Profile  = profileserializer(read_only = True)

    class Meta:
        model = User
        fields = ["id","is_active","Profile"]
