from django.urls import path
from .views import ClientCreateView, ClientListView, ClientDetailView, ClientUpdateDeleteView, ClientSessionUpdateView

urlpatterns = [
    path("create/", ClientCreateView.as_view(), name="client_create"),
    path("",ClientListView.as_view(), name="client_list"),
    path("details/<uuid:pk>/", ClientDetailView.as_view(), name="client_details"),
    path("edit/<uuid:id>/", ClientUpdateDeleteView.as_view(), name="client_edit"),
    path("update_sess/<uuid:id>/", ClientSessionUpdateView.as_view(), name="client_session_update")
]