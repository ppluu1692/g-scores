from django.urls import path
from .views import CheckScoreView, ReportView, TopA00View

urlpatterns = [
    path("api/check-score/<str:sbd>/", CheckScoreView.as_view(), name="check-score"),
    path("api/reports/", ReportView.as_view(), name="reports"),
    path("api/top-a00/", TopA00View.as_view(), name="top-a00"),
]
