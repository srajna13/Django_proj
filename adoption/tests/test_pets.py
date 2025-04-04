import pytest
from rest_framework.test import APIClient
from adoption.models import Pet
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_get_pets():
    client = APIClient()
    response = client.get("/api/pets/")
    assert response.status_code == 401  # Unauthorized


@pytest.mark.django_db
def test_admin_can_add_pet():
    admin = User.objects.create_user(
        username="admin", email="admin@example.com", password="adminpass", is_staff=True
    )
    client = APIClient()
    client.force_authenticate(user=admin)

    response = client.post(
        "/api/admin/pets/",
        {"name": "Buddy", "age": 3, "breed": "Golden Retriever", "available": True},
        format="json",
    )

    assert response.status_code == 201
    assert response.data["name"] == "Buddy"
