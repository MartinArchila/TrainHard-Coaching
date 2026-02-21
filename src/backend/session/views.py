from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticated
from .models import Session
from .serializers import CreateSessionSerializer, ReadSessionSerializer, UpdateSessionSerializer

class CreateSessionView(generics.CreateAPIView):
    queryset = Session.objects.all()
    serializer_class = CreateSessionSerializer
    permission_classes = [IsAuthenticated]

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