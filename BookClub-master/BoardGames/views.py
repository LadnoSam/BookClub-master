from django.views.generic import DetailView, ListView

from .models import Author, Boardgame, Genre


class AuthorDetailView(DetailView):
    model = Author


class AuthorListView(ListView):
    model = Author
    paginate_by = 10


class BookDetailView(DetailView):
    model = Boardgame


class BookListView(ListView):
    model = Boardgame
    paginate_by = 10


class GenreDetailView(DetailView):
    model = Genre


class GenreListView(ListView):
    model = Genre
    paginate_by = 10
