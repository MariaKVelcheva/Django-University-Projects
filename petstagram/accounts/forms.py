from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from petstagram.accounts.models import UserModel, Profile


class AppUserChangeForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = "__all__"


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
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"autofocus": True,
                   "placeholder": "Email"},
        ),
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current_password",
                   "placeholder": "Password"},

        )
    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "date_of_birth", "profile_picture", )

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "date_of_birth": "Date of Birth",
            "profile_picture": "Profile Picture",
        }
