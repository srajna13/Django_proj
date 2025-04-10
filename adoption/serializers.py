from rest_framework import serializers
from .models import User, Pet, Adoption


class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.CharField(
        source="get_role_display", read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role_display"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)  # 🔒 This hashes the password
        user.save()
        return user


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"


class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = "__all__"
