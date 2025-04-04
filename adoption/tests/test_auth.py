import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.mark.django_db
def test_user_signup():
    client = APIClient()
    response = client.post(
        "/api/auth/signup/",
        {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpass123",
        },
        format="json",
    )

    assert response.status_code == 201
    assert response.data["username"] == "testuser"


@pytest.mark.django_db
def test_user_login():
    user = User.objects.create_user(
        username="testuser", email="testuser@example.com", password="testpass123"
    )
    client = APIClient()

    response = client.post(
        "/api/auth/login/",
        {"username": "testuser", "password": "testpass123"},
        format="json",
    )

    assert response.status_code == 200
    assert "access" in response.data
