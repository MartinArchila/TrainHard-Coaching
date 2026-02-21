from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Coach

#Serializer for creating Coach object
class CoachCreateSerializer(serializers.ModelSerializer):
    #Input fields for creating User Model
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)

    #Read-only fields for API Response
    user_username = serializers.CharField(source="user.username", read_only=True)
    user_email = serializers.EmailField(source="user.email",read_only=True)
    users_name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Coach
        fields = [
            "first_name",
            "last_name",
            "username",
            "users_name",
            "user_username",
            "password",
            "email",
            "user_email",
            "is_head_coach",
            "address",
            "phone_num",
        ]

    def get_users_name(self,obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def create(self, validated_data):
        #Extract User Fields
        username = validated_data.pop("username")
        password = validated_data.pop("password")
        email = validated_data.pop("email", "")
        first_name = validated_data.pop("first_name")
        last_name = validated_data.pop("last_name")

        #Create user Object
        user = User.objects.create_user(
            username = username, password = password, email = email, first_name = first_name, last_name = last_name
        )

        #Create Coach Object
        coach = Coach.objects.create(
            user=user, **validated_data
        )

        return coach
    
class CoachReadSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    username = serializers.CharField(source="user.username",read_only=True)
    email = serializers.EmailField(source="user.email",read_only=True)
    class Meta:
        model = Coach
        fields = [
            "id",
            "username",
            "name",
            "email",
            "is_head_coach",
            "address",
            "phone_num",
        ]

    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
class CoachUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    class Meta:
        model = Coach
        fields = [
        "first_name",
        "last_name",
        "email",
        "phone_num",
        "address",
        ]

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user",{})

        instance.phone_num = validated_data.get(
            "phone_num", instance.phone_num
        )
        instance.address = validated_data.get(
            "address", instance.address
        )
        instance.save()

        user = instance.user
        user.first_name = user_data.get("first_name",user.first_name)
        user.last_name = user_data.get("last_name",user.last_name)
        user.email = user_data.get("email",user.email)

        return instance
    
