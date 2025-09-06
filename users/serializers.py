from rest_framework import serializers
from .models import AppUser
from django.contrib.auth.hashers import check_password
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['user_id', 'first_name', 'last_name', 'user_type', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}
class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        phone_number = data.get("phone_number")
        password = data.get("password")
        try:
            user = AppUser.objects.get(phone_number=phone_number)
        except AppUser.DoesNotExist:
            raise serializers.ValidationError("User not found")
        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid credentials")
        data["user"] = user
        return data
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['user_id', 'first_name', 'last_name', 'user_type', 'phone_number', 'created_at']