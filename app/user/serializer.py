from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Account
from .exception import UserNotFound, NoEmailProvided, UserNotActive


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, min_length=6)
    token = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Account

        fields = (
            "email",
            "password",
            "id",
            "firstname",
            "lastname",
            "profile_picture",
            "token",
        )

    def create(self, validate_data):
        return Account.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    id = serializers.CharField(max_length=128, read_only=True)
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        """
        Validates the data passed to the login/
        """

        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise NoEmailProvided

        account = authenticate(email=email, password=password)

        if account is None:
            raise UserNotFound

        if not account.is_active:
            raise UserNotActive

        return {
            "id": account.id,
            "email": account.email,
            "token": account.token,
            "firstname": account.firstname,
            "lastname": account.lastname,
            "profile_picture": account.profile_picture,
        }

    class Meta:
        model = Account
        fields = (
            "email",
            "password",
            "token",
            "id",
            "firstname",
            "lastname",
            "profile_picture",
        )
        read_only_fields = (
            "id",
            "token",
            "firstname",
            "lastname",
            "profile_picture",
        )


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = Account
        fields = (
            "email",
            "password",
            "token",
            "id",
            "firstname",
            "lastname",
            "profile_picture",
        )
        read_only_fields = ("token",)

    def update(self, instance, validate_data):
        password = validate_data.pop("password", None)

        for (key, value) in validate_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "email",
            "password",
            "token",
            "id",
            "firstname",
            "lastname",
            "profile_picture",
        )


class AccountEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance
