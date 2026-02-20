from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('logout/', views.AppUserLogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('delete/', views.AppUserDeleteView.as_view(), name='delete-profile'),
        path('edit/', views.ProfileEditPageView.as_view(), name='edit-profile'),
        path('details/', views.AppUserDetailView.as_view(), name='details-profile'),
    ])),
]

