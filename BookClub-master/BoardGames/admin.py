from django.contrib import admin
from .models import Author, Boardgame, Genre, BoardGame, Loan


admin.site.register(Author)  
admin.site.register(Boardgame)  
admin.site.register(Genre)  


@admin.register(BoardGame)  
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_at", "updated_at")
    search_fields = ("name", "owner__username")


@admin.register(Loan)  
class LoanAdmin(admin.ModelAdmin):
    list_display = ("board_game", "borrower", "loan_date", "return_date")
    list_filter = ("loan_date", "return_date")
