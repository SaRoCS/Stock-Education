from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from colorfield.fields import ColorField


class User(AbstractUser):
    cash = models.DecimalField(default=10000.00, decimal_places=2, max_digits=9)
    teacher = models.BooleanField(default=False)
    is_in_class = models.BooleanField(default=False)
     

class Stocks(models.Model):
    symbol = models.CharField(max_length=5)
    amount = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name="stocks")

    class Meta:
        unique_together = ['user', 'symbol']
    
    def __str__(self):
        return f"{self.user.username}|{self.symbol}"


class Transaction(models.Model):
    buyer = models.ForeignKey(User, on_delete=CASCADE, related_name='transactions')
    symbol = models.CharField(max_length=5)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    amount = models.IntegerField(default=1)
    date = date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.username}|{self.symbol}|{self.date}"


class Classroom(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class_id = models.CharField(max_length=7, unique=True)
    member = models.ManyToManyField(User, related_name="classroom")
    cash = models.DecimalField(default=10000.00, decimal_places=2, max_digits=9)

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    name = models.CharField(max_length=100, unique=False)
    member = models.ManyToManyField(User, related_name="team")
    classroom = models.ForeignKey(Classroom, on_delete=CASCADE, related_name="teams")
    color = ColorField(default="#0000EE")

    def __str__(self):
        return f"{self.name}"

