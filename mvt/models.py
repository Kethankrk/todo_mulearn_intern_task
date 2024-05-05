from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None



class Todo(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)
