from django.db import models
from django.contrib.auth.models import User
import uuid

class Coach (models.Model):
    id = models.UUIDField (
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    #OneToOne Relationships with native User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_head_coach = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True,editable=True)
    phone_num = models.CharField(max_length=11, blank=False, editable=True)

    def __str__(self):
        return self.user.get_full_name()