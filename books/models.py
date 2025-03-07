from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    condition = models.CharField(max_length=20, choices=[('New', 'New'), ('Used', 'Used')])
    exchange_type = models.CharField(max_length=50, choices=[('Swap', 'Swap'), ('Giveaway', 'Giveaway')], default='Swap')
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class BookRequest(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Request for {self.book.title} by {self.requester.username}'
