from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from AuditLog.services.audit_service import log_event
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        request = self.context.get("request")

        try:
            data = super().validate(attrs)
        except:
            log_event(
                request=request,
                user=None,
                event_type="LOGIN_FAILED",
                description=f"Failed login attempt for {attrs.get('username')}"
            )
            raise
        
        log_event(
            request=request,
            user=self.user,
            event_type="LOGIN",
            description="JWT login successful"
        )

        return data

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    
    def validate(self, attrs):
        request = self.context.get("refresh")
        refresh_token_str = attrs.get("refresh")

        try:
            data = super().validate(attrs)

            refresh = RefreshToken(refresh_token_str)
            user_id = refresh["user_id"]
            user= User.objects.filter(id=user_id).first()

            log_event(
                request=request,
                user=user,
                event_type="TOKEN_REFRESH",
                description="JWT access token refreshed successfully"
            )

        except Exception:
            log_event(
                request=request,
                user=None,
                event_type="TOKEN_REFRESH_FAILED",
                description="Failed attempt to refresh JWT Token"
            )
            raise
        
        return data
        
