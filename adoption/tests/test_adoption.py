import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from adoption.models import Pet, Adoption

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
    return Pet.objects.create(name="Max", age=2, species="Labrador", available=True)

@pytest.fixture
def adopted_pet(user):
    pet = Pet.objects.create(name="Bella", age=4, species="Beagle", available=False)
    Adoption.objects.create(user=user, pet=pet)
    return pet


@pytest.mark.django_db
def test_user_can_adopt_pet():
    user = User.objects.create_user(
        username="testuser", email="testuser@example.com", password="testpass123"
    )
    pet = Pet.objects.create(
        name="Max", age=2, species="Labrador", available=True)

    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post(f"/api/pets/{pet.id}/adopt/")
    assert response.status_code == 200
    assert response.data["message"] == "Pet adopted successfully!"

    pet.refresh_from_db()
    assert pet.available == False

# trying to adopt a pet again
@pytest.mark.django_db
def test_user_cannot_adopt_same_pet_twice(client, adopted_pet):
    response = client.post(f"/api/pets/{adopted_pet.id}/adopt/")
    assert response.status_code == 400
    assert "already adopted" in response.data.get("error","").lower()

# Edge case: unauthenticated user cannot adopt
@pytest.mark.django_db
def test_unauthenticated_user_cannot_adopt(adopted_pet):
    client = APIClient()
    response = client.post(f"/api/pets/{adopted_pet.id}/adopt/")
    assert response.status_code == 401  # Unauthorized
    assert"credentials" in response.data.get("detail","").lower()
