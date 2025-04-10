import pytest
from rest_framework.test import APIClient
from adoption.models import Pet, Adoption
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def user():
    return User.objects.create_user(
        username="testuser", email="testuser@example.com", password="testpass123"
    )

@pytest.fixture
def client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def available_pet():
    return Pet.objects.create(name="Leo", age=2, species="Cat", available=True)

@pytest.fixture
def adopted_pet(user):
    pet = Pet.objects.create(name="Rocky", age=5, species="Dog", available=False)
    Adoption.objects.create(user=user, pet=pet)
    return pet


@pytest.mark.django_db
def test_get_pets():
    client = APIClient()
    response = client.get("/api/pets/")
    assert response.status_code == 401  # Unauthorized

# try adopting already adopted pet:
@pytest.mark.django_db
def test_cannot_adopt_unavailable_pet(client, adopted_pet):
    response = client.post(f"/api/pets/{adopted_pet.id}/adopt/")
    assert response.status_code == 400
    assert "already adopted" in response.data["error"].lower()