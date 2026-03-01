from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from .models import Session
from .serializers import CreateSessionSerializer, ReadSessionSerializer, UpdateSessionSerializer
from AuditLog.services.audit_service import log_event

class CreateSessionView(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = CreateSessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        session = serializer.save()

        log_event(
            request= self.request,
            user=self.requesst.user,
            event_type="SESSION_SCHEDULED",
            description="Session scheduled successfully"
        )

class ListSessionView(generics.ListAPIView):
    queryset = Session.objects.all()
    serializer_class = ReadSessionSerializer
    permission_classes = [IsAuthenticated]

class DetailSessionView(generics.RetrieveAPIView):
    queryset = Session.objects.all()
    serializer_class = ReadSessionSerializer
    permission_classes = [IsAuthenticated]

class SessionUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = UpdateSessionSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        session = serializer.save()

        log_event(
            request=self.request,
            user=self.request.user,
            event_type="SCHEDULED_EDIT",
            description="Session updated successfully"
        )

    def perform_destroy(self, instance):
        session = instance
        instance.delete()

        log_event(
            request=self.request,
            user=self.request.user,
            event_type="SESSION_DELETE",
            description="Session deleted"
        )