from django.urls import path
from .views import CoachCreateView, CoachListView, CoachDetailView, CoachUpdateDeleteView

urlpatterns = [
    path("coach/", CoachCreateView.as_view(), name="coach-create"),
    path("coaches/",CoachListView.as_view(), name = "coach_list"),
    path("coach/<uuid:pk>/", CoachDetailView.as_view(), name="coach_details"),
    path("coaches/<uuid:id>/",CoachUpdateDeleteView.as_view(), name="coach-update-delete"),
]