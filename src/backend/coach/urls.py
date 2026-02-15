from django.urls import path
from .views import CoachCreateView, CoachListView, CoachDetailView, CoachUpdateDeleteView

urlpatterns = [
    path("create/", CoachCreateView.as_view(), name="coach-create"),
    path("list/",CoachListView.as_view(), name = "coach_list"),
    path("details/<uuid:pk>/", CoachDetailView.as_view(), name="coach_details"),
    path("edit/<uuid:id>/",CoachUpdateDeleteView.as_view(), name="coach-update-delete"),
]