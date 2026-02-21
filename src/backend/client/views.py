from django.shortcuts import render
from rest_framework import generics
from .models import Client
from .serializers import ClientCreateSerializer, ClientReadSerializer, ClientInfoUpdateSerializer, ClientSessionInfoUpdateSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticated

# Create your views here.
class ClientCreateView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes= [IsAuthenticated]

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

class ClientSessionUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSessionInfoUpdateSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticated]