from django.shortcuts import render
from rest_framework import generics
from .models import Coach
from .serializers import CoachCreateSerializer, CoachReadSerializer, CoachUpdateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CoachCreateView(generics.CreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachCreateSerializer
    permission_classes = [AllowAny]

class CoachListView(generics.ListAPIView):
    queryset = Coach.objects.all()
    serializer_class=CoachReadSerializer
    permission_classes = [AllowAny]

class CoachDetailView(generics.RetrieveAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachReadSerializer
    permission_classes = [AllowAny]

class CoachUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachUpdateSerializer
    lookup_field = "id"
    permission_classes = [AllowAny]