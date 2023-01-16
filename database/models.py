from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from uuid import uuid4

# X------------X------------X
# user model
# X------------X------------X
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    last_update = models.CharField(max_length=100)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sub = models.CharField(max_length=100)
    sid = models.CharField(max_length=100)
    picture = models.CharField(max_length=500, null=True, blank=True)

# X------------X------------X
# user-group model
# X------------X------------X
class UserGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    last_update = models.CharField(max_length=100)
    
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(to="database.User", null=False, blank=False, on_delete=models.CASCADE, related_name="admin")
    users = models.ManyToManyField(to="database.User", related_name="users")