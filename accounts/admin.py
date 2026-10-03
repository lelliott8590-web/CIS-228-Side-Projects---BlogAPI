from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

from .models import Customuser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Customuser
    list_display = [
        "email",
        "username",
        "is_staff",
        "is_active",
    ]

admin.site.register(Customuser, CustomUserAdmin)
