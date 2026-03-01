from django.db import models
from django.contrib.auth.models import User
import uuid

class AuditLog(models.Model):

    EVENT_TYPES = [
        ("USER_CREATED", "Coach Created"),
        ("LOGIN","Logged in"),
        ("LOGIN_FAILED","Failed Login Attempt"),
        ("LOGOUT", "Logged out"),
        ("TOKEN_REFRESH", "Token Refeshed"),
        ("TOKEN_REFRESH_FAILED", "Token Refreshed Failed"),
        ("SESSION_SCHEDULED", "Session scheduled"),
        ("SESSION_COMPLETED", "Session completed"),
        ("SESSION_EDIT", "Session modified "),
        ("SESSION_DELETE", "Session eliminated"),
        ("CLIENT_CREATE", "Client created"),
        ("CLIENT_EDIT","Client modified"),
        ("CLIENT_DELETE","Client eliminated"),
        ("COACH_CREATE", "Coach created"),
        ("COACH_EDIT","Coach modified"),
        ("COACH_DELETE","Coach eliminated"),

    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="audit_logs")
    event_type = models.CharField(max_length=100, choices = EVENT_TYPES)
    model_name = models.CharField(max_length=100, null=True, blank=True)
    object_id = models.CharField(max_length=110, null=True, blank=True)
    description = models.CharField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.id}, {self.user}, {self.event_type}, {self.model_name}, {self.object_id}, {self.description}, {self.ip_address}, {self.user_agent}, {self.timestamp}"



