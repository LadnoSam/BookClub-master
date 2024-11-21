from django.urls import path

from . import views


urlpatterns = [
    path("authors/", views.AuthorListView.as_view(), name="author-list"),
    path("authors/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
    path("BoardGames/", views.BookListView.as_view(), name="boardgame-list"),
    path("BoardGames/<int:pk>", views.BookDetailView.as_view(), name="boardgame-detail"),
    path("BoardGames/", views.GenreListView.as_view(), name="genre-list"),
    path("BoardGames/<int:pk>", views.GenreDetailView.as_view(), name="genre-detail"),
]
