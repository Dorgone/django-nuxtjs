from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from rest_framework import serializers, validators

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        write_only=True, validators=[validators.UniqueValidator(
            message = 'This email already exists',
            queryset = CustomUser.objects.all()
        )]
    )
    password = serializers.CharField(write_only=True)
    last_name = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 
                    'last_name', 
                    'email',
                    'password', 
                    'is_superuser',
                    'is_staff',
                    )


class CustomUserRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('first_name', 
                    'last_name', 
                    'email',
                    'is_superuser',
                    'is_staff',
                    'id')