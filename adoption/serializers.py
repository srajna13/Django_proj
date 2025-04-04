from rest_framework import serializers
from .models import User, Pet, Adoption


class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.CharField(
        source="get_role_display", read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "role_display"]

    def create(self, validated_data):
        validated_data["role"] = "user"

        # default role
        return super().create(validated_data)


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"


class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = "__all__"
