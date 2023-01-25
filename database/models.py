from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from uuid import uuid4

# X------------X------------X
# users model
# X------------X------------X
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sub = models.CharField(max_length=100)
    sid = models.CharField(max_length=100)
    picture = models.CharField(max_length=500, null=True, blank=True)

    places = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    last_update = models.CharField(max_length=100, default='create')

# X------------X------------X
# trips model
# X------------X------------X
class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    name = models.CharField(max_length=100)
    destination_place = models.TextField(null=True, blank=True)
    
    admin = models.ForeignKey(to="database.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="trip_admin")
    users = models.ManyToManyField(to="database.User", related_name="trip_users", blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    last_update = models.CharField(max_length=100, default='create')

# X------------X------------X
# places model
# X------------X------------X
class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    
    name = models.CharField(max_length=100)
    pincode = models.IntegerField()
    google_map_link = models.TextField()
    
    admin = models.ForeignKey(to="database.User", null=True, blank=True, on_delete=models.SET_NULL, related_name="places_admin")
    users = models.ManyToManyField(to="database.User", related_name="places_users")

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    last_update = models.CharField(max_length=100, default='create')