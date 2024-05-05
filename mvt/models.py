from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    first_name = None
    last_name = None



class Todo(models.Model):
    title = models.CharField(max_length=40)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    expire = models.DateTimeField()
    user = models.ForeignKey(User, related_name="todos", on_delete=models.CASCADE)

    @property
    def is_expired(self):
        return self.expire < timezone.now()

    class Meta:
        ordering = ['-expire']