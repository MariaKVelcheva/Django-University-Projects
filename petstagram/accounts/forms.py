from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from petstagram.accounts.models import UserModel


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel


