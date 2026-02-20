from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, DetailView

from petstagram.accounts.forms import AppUserCreationForm, AppUserLoginForm, ProfileEditForm
from petstagram.accounts.models import Profile

UserModel = get_user_model()


class AppUserLoginView(LoginView):
    form_class = AppUserLoginForm
    template_name = 'accounts/login-page.html'

    def form_valid(self, form):
        super().form_valid(form)
        profile_instance, _ = Profile.objects.get_or_create(user=self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class AppUserDeleteView(LoginRequiredMixin, DeleteView):
    model = UserModel
    success_url = reverse_lazy("home")
    template_name = 'accounts/profile-delete-page.html'

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())


class AppUserDetailView(DetailView):
    model = UserModel
    template_name = 'accounts/profile-details-page.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_likes_count"] = sum(p.likes_count() for p in self.object.photos.all())
        return context


class ProfileEditPageView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit-page.html'
    form_class = ProfileEditForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy(
            "details-profile",
            kwargs={"pk": self.object.pk}
        )


class AppUserRegisterView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('login')


class AppUserLogoutView(LoginRequiredMixin, LogoutView):
    pass

