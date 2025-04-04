from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Pet, Adoption, User
from .serializers import PetSerializer, AdoptionSerializer, UserSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsAdminUser


class AdminOnly(permissions.BasePermission):
    """Custom permission to allow only admins to access a view."""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"


class SignupView(APIView):
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        data = request.data.copy()
        data["role"] = data.get("role", "user")

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD
                ),
            },
            required=["username", "password"],
        )
    )
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"error": "Invalid username or password."}, status=401)

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }
        )


class PetListView(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [IsAdminUser]


class AdoptionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pet_id):
        pet = get_object_or_404(Pet, id=pet_id)
        if not pet.available:
            return Response({"error": "Pet already adopted"}, status=400)

        Adoption.objects.create(user=request.user, pet=pet)
        pet.available = False
        pet.save()
        return Response({"message": "Pet adopted successfully!"})


class AvailablePetsListView(generics.ListAPIView):
    queryset = Pet.objects.filter(available=True)  # Only available pets
    serializer_class = PetSerializer
    # Any logged-in user can see
    permission_classes = [permissions.IsAuthenticated]


def home_view(request):
    return JsonResponse({"message": "Welcome to the Pet Adoption System API!"})
