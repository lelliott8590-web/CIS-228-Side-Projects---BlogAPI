from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import Customuser

class CustomUserCreationForm(AdminUserCreationForm):

    class meta:
        model = Customuser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class meta:
        model = Customuser
        fields = ("username", "email")