from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):...

class Secret(models.Model):
    login = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='secrets')

class Message(models.Model):
    name = models.CharField(max_length=150)
    dt_depart = models.DateTimeField()
    dt_receipt = models.DateTimeField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    


class Attach(models.Model):
    file = models.CharField(max_length=256)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attachs')

