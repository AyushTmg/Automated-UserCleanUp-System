from django.urls import path
from .views import (
    CleanupReportListView, 
    ManualCleanUpTriggerView
)


urlpatterns = [
    path('reports/latest/', CleanupReportListView.as_view(), name='cleanup-reports'),
    path('cleanup/trigger/', ManualCleanUpTriggerView.as_view(), name='manual-cleanup-trigger'),
]