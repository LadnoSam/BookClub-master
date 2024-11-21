from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Boardgame(models.Model):  
    title = models.CharField(max_length=200, db_index=True)
    subtitle = models.CharField(max_length=200, blank=True)
    author = models.ManyToManyField("Author")
    description = models.TextField(max_length=1000, null=True)
    pub_year = models.PositiveSmallIntegerField("Publication Year", null=True)
    genre = models.ManyToManyField("Genre")

    @property
    def verbose_title(self):
        pub_year = f" ({self.pub_year})" if self.pub_year else ""
        subtitle = f": {self.subtitle}" if self.subtitle else ""
        return f"{self.title}{subtitle}{pub_year}"

    def __str__(self):
        return self.title + (f" ({str(self.pub_year)})" if self.pub_year else "")


class Author(models.Model):  
    last_name = models.CharField(max_length=100, db_index=True)
    given_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        birth_year = self.date_of_birth.year if self.date_of_birth else ""
        death_year = self.date_of_death.year if self.date_of_death else ""
        lifespan = f" ({birth_year}-{death_year})" if birth_year or death_year else ""
        full_name = f"{self.last_name}" + (f", {self.given_name}" if self.given_name else "")
        return f"{full_name}{lifespan}"

    class Meta:
        ordering = ["last_name", "given_name", "date_of_birth"]


class Genre(models.Model):  
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class BoardGame(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    characteristics = models.CharField(max_length=200, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_games")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Loan(models.Model):
    board_game = models.ForeignKey(BoardGame, on_delete=models.CASCADE, related_name="loans")
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrowed_games")
    loan_date = models.DateTimeField(default=now)
    return_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.board_game.name} borrowed by {self.borrower.username}"

    def save(self, *args, **kwargs):
        active_loans = Loan.objects.filter(borrower=self.borrower, return_date__isnull=True)
        if active_loans.count() >= 3:
            raise ValueError("Cannot borrow more than 3 games simultaneously. Please return a game first.")
        super().save(*args, **kwargs)
