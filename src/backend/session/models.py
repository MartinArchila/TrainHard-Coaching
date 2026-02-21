from django.db import models
from django.utils import timezone
from coach.models import Coach
from client.models import Client
import uuid

class Session (models.Model):
    #Session length by minutes
    SHORT_SESSION = 30
    LONG_SESSION = 60

    SESSION_CHOICES = [
        (SHORT_SESSION, "30 minutes"),
        (LONG_SESSION, "1 hour")
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, related_name="sessions")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="sessions")
    session_length = models.IntegerField(choices=SESSION_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
