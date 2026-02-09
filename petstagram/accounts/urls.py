from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('register/', views.RegisterPageView.as_view(), name='register'),
    path('delete/', views.ProfileDeleteView.as_view(), name='delete-profile'),
    path('edit/', views.ProfileEditPageView.as_view(), name='edit-profile'),
    path('details/', views.ProfileDetailsPageView.as_view(), name='details-profile'),
]

