from django.urls import path, include
from petstagram.photos import views

urlpatterns = [
    path('create/', views.PhotoAddView.as_view(), name='create-photo'),
    path('details/', views.PhotoDetailsView.as_view(), name='details-photo'),
    path('edit/', views.PhotoEditView.as_view(), name='edit-photo'),
]

