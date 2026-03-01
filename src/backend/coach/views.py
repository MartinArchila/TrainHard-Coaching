from django.shortcuts import render
from rest_framework import generics
from .models import Coach
from .serializers import CoachCreateSerializer, CoachReadSerializer, CoachUpdateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from AuditLog.services.audit_service import log_event

class CoachCreateView(generics.CreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        coach = serializer.save()

        log_event(
            request=self.request,
            user=self.request.user,
            event_type="COACH_CREATED",
            description=f"Coach profile {coach.user.username} created"
        )

class CoachListView(generics.ListAPIView):
    queryset = Coach.objects.all()
    serializer_class=CoachReadSerializer
    permission_classes = [IsAuthenticated]

class CoachDetailView(generics.RetrieveAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachReadSerializer
    permission_classes = [IsAuthenticated]

class CoachUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachUpdateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        coach = serializer.save()

        log_event(
            request=self.request,
            user=self.request.user,
            event_type="COACH_EDIT",
            description=f"Coach profile {coach.user.username} information updated"
        )

    def perform_destroy(self, instance):
        username = instance.user.username
        instance.delete()

        log_event(
            request=self.request,
            user=self.request.user,
            event_type="COACH_DELETE",
            description=f"Coach profile {username} eliminated"
        )