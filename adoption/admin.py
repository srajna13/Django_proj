from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Pet, Adoption

admin.site.register(User, UserAdmin)  # Register User model with admin
admin.site.register(Pet)  # Register Pet model
admin.site.register(Adoption)  # Register Adoption model


# user1234 - 12abcd34
# super user: user - user
