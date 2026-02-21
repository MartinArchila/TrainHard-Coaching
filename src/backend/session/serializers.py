from rest_framework import serializers
from coach.models import Coach
from client.models import Client
from .models import Session

#Create Serializer for Session Objects
class CreateSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = [
            "coach",
            "client",
            "session_length",
            "start_time",
            "end_time",
            "date"
        ]

#Read Serializer for Session Objects
class ReadSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

#Update Serializer for Session Objects
class UpdateSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"