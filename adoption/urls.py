from django.urls import path
from .views import (
    LogoutView,
    SignupView,
    LoginView,
    PetListView,
    AdoptionView,
    AvailablePetsListView,
)

urlpatterns = [
    path("auth/signup/", SignupView.as_view(), name="signup"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("pets/", AvailablePetsListView.as_view(), name="available-pets"),
    path("pets/<int:pet_id>/adopt/", AdoptionView.as_view(), name="adopt_pet"),
]
