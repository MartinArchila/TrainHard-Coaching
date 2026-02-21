from django.db import models
from django.core.validators import MinValueValidator
from coach.models import Coach
import datetime
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, related_name="clients")
    first_name = models.CharField('First Name',max_length=255)
    last_name = models.CharField('Last_Name',max_length=255)
    phone_num = models.CharField(max_length=11,null=True,blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    session_credits = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    last_session_date = models.DateField(default=datetime.date.today)
    sessions_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name