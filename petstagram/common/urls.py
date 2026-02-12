from django.urls import path, include

from petstagram.common import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('like/<int:photo_id>/', views.like_functionality, name='like'),
]

