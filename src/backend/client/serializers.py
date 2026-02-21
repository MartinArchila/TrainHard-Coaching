from rest_framework import serializers
from coach.models import Coach
from .models import Client

#Serializer to Create Client
class ClientCreateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    name = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'name',
            'coach',
            'phone_num',
            'email',
            'session_credits',
            'last_session_date',
            'sessions_completed',
        ]

    def get_name(self,obj):
        return f'{obj.first_name} {obj.last_name}'

#Serializer to read Client Information
class ClientReadSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    coach = serializers.PrimaryKeyRelatedField(
        queryset = Coach.objects.all(),
        required = False,
        allow_null= True
    )

    class Meta:
        model = Client
        fields = [
            'id',
            'name',
            'coach',
            'phone_num',
            'email',
            'session_credits',
            'last_session_date',
            'sessions_completed',
        ]
    
    def get_name(self,obj):
        return f'{obj.first_name} {obj.last_name}'

#Serializer to update/delete Client Information
class ClientInfoUpdateSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)

    coach = serializers.PrimaryKeyRelatedField(
        queryset = Coach.objects.all(),
        required = False,
        allow_null= True
    )

    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'name',
            'coach',
            'phone_num',
            'email',
        ]

    def get_name(self,obj):
        return f'{obj.first_name} {obj.last_name}'

#Serializer to update the session(s) related information of the client
class ClientSessionInfoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'session_credits',
            'last_session_date',
            'sessions_completed',
        ]
