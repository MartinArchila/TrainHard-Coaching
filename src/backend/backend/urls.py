from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomTokenObtainPairView, CustomTokenRefreshView
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("login/", TokenObtainPairView.as_view(), name="get_token"),
    # path("auth/refresh/", TokenRefreshView.as_view(),name="refresh_token"),
    path("login/", CustomTokenObtainPairView.as_view(), name="get_token"),
    path("auth/refresh/", CustomTokenRefreshView.as_view(),name="refresh_token"),
    path("coach/", include("coach.urls")),
    path("client/", include("client.urls")),
    path("session/", include("session.urls")),
]
