from django.views.generic import DetailView, ListView

from .models import Author, BoardGame, Genre


class AuthorDetailView(DetailView):
    model = Author


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class BookDetailView(DetailView):
    model = BoardGame


class BookListView(ListView):
    model = BoardGame
    paginate_by = 10


class GenreDetailView(DetailView):
    model = Genre


class GenreListView(ListView):
    model = Genre
    paginate_by = 10
