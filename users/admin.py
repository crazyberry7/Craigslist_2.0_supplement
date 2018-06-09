from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import customuser

# Register your models here.
"""
from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):

    model = CustomUser
    add_form = CustomUserCreationForm

"""
admin.site.register(customuser)

