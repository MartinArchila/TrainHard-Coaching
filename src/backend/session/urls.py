from django.urls import path
from .views import CreateSessionView, ListSessionView, DetailSessionView, SessionUpdateDeleteView
urlpatterns = [
    path("create/", CreateSessionView.as_view(), name = "create_session"),
    path("", ListSessionView.as_view(), name = "session_list"),
    path("detail/<uuid:pk>/", DetailSessionView.as_view(), name="detail_session"),
    path("edit/<uuid:id>/",SessionUpdateDeleteView.as_view(),name="edit_session"),
]