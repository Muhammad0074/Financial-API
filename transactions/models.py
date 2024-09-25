from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    transaction_date = models.DateTimeField()
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.description}"
