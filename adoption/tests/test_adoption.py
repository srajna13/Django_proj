import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from adoption.models import Pet, Adoption

User = get_user_model()


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
