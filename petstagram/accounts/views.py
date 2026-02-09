from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = 'accounts/login-page.html'


class ProfileDeleteView(TemplateView):
    template_name = 'accounts/profile-delete-page.html'


class ProfileDetailsPageView(TemplateView):
    template_name = 'accounts/profile-details-page.html'


class ProfileEditPageView(TemplateView):
    template_name = 'accounts/profile-edit-page.html'


class RegisterPageView(TemplateView):
    template_name = 'accounts/register-page.html'
