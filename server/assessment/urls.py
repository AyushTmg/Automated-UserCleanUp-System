from django.urls import path
from .views import (
    CleanupReportListView, 
    ManualCleanUpTriggerView
)


urlpatterns = [
    path('cleanup-reports/', CleanupReportListView.as_view(), name='cleanup-reports'),
    path('trigger/', ManualCleanUpTriggerView.as_view(), name='manual-cleanup-trigger'),
]