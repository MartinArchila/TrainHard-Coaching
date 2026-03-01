from django.shortcuts import render
from rest_framework import generics
from .models import Client
from .serializers import ClientCreateSerializer, ClientReadSerializer, ClientInfoUpdateSerializer, ClientSessionInfoUpdateSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from AuditLog.services.audit_service import log_event

# Create your views here.
class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes= [IsAuthenticated]

    def perform_create(self,serializer):
        client = serializer.save()

        log_event(
            request=self.request,
            user=self.request.user,
            event_type="CLIENT_CREATE",
            description=f"Client {client.first_name} {client.last_name} created"
        )

class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientReadSerializer
    permission_classes = [IsAuthenticated]

class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientReadSerializer
    permission_classes = [IsAuthenticated]

class ClientUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientInfoUpdateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]

    def perform_update(self,serializer):
        client = serializer.save()

        log_event(
            request= self.request,
            user= self.request.user,
            event_type="CLIENT_EDIT",
            description=f"Client {client.first_name} {client.last_name} information updated"
        )

    def perform_destroy(self, instance):
        name = instance.first_name + " " + instance.last_name
        instance.delete()

        log_event(
            request = self.request,
            user=self.request.user,
            event_type="CLIENT_DELETE",
            description=f"Client {name} eliminated"
        )

#This View will be the endpoint that is used to update the session information tied to the client
#independently from the rest of the client information
class ClientSessionUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSessionInfoUpdateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]