from django.contrib import admin

from .models import Author, Boardgame, Genre


admin.site.register(Author)
admin.site.register(Boardgame)
admin.site.register(Genre)
