from django.db import models
from django.conf import settings  # Import settings to access User model

# Book model for storing book details
class Book(models.Model):
    CONDITION_CHOICES = [('New', 'New'), ('Used', 'Used')]
    EXCHANGE_TYPE_CHOICES = [('Swap', 'Swap'), ('Giveaway', 'Giveaway')]

    title = models.CharField(max_length=200)  # Book title
    author = models.CharField(max_length=100)  # Book author
    genre = models.CharField(max_length=100)  # Book genre
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)  # New/Used
    exchange_type = models.CharField(max_length=10, choices=EXCHANGE_TYPE_CHOICES)  # Swap or giveaway
    location = models.CharField(max_length=100)  # Where the book is available
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # User who owns the book

    def __str__(self):
        return self.title  # Return book title as default string