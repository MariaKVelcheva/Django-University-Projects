from django.urls import path
from petstagram.books_api import views


urlpatterns = [
    path("/", views.ListBooksView.as_view(), name="list-books"),
    path('book/<int:pk>/', views.DetailBookSetView.as_view(), name="detail-book"),
]