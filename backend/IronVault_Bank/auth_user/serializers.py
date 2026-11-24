# auth_user/serializers.py

from rest_framework import serializers
from account.serializers import AccountDetailSerializer
from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    accounts = AccountDetailSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "profile_picture_url",
            "is_active",
            "roles",
            "created_at",
            "updated_at",
        ]


class ForgotPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordRequestSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=128)
    new_password = serializers.CharField()


class RegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "password",
        ]

class LoginRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    roles = serializers.ListField(child=serializers.IntegerField())


class UpdatePasswordRequestSerializer(serializers.Serializer):
    password = serializers.CharField()
    new_password = serializers.CharField()