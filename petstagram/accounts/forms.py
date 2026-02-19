from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from petstagram.accounts.models import UserModel


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email", )

        widgets = {
            "email": forms.EmailInput(
                attrs={'placeholder': 'Email'}
            ),

            "password1": forms.PasswordInput(
                attrs={'placeholder': 'Password'}
            ),

            "password2": forms.PasswordInput(
                attrs={"placeholder": "Repeat password"}
            ),
        }


class AppUserLoginForm(AuthenticationForm):
    emails = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"autofocus": True}),
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current_password"},
        )
    )