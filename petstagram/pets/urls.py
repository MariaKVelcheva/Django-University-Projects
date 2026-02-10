from django.urls import path, include

from petstagram.pets import views

urlpatterns = [
    path('create/', views.PetAddView.as_view(), name='create-pet'),
    path('<int:pk>/', include([
        path('delete/', views.PetDeleteView.as_view(), name='delete-pet'),
        path('details/', views.PetDetailsView.as_view(), name='details-pet'),
        path('edit/', views.PetEditView.as_view(), name='edit-pet'),
    ]))
]
