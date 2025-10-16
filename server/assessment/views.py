from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from assessment.tasks import cleanup_inactive_users
from utils.response.response import CustomResponse as cr
from .models import CleanupReport
from .serializers import CleanupReportSerializer

class CleanupReportListView(ListAPIView):
    queryset = CleanupReport.objects.all().order_by('-timestamp')
    serializer_class = CleanupReportSerializer
 
class ManualCleanUpTriggerView(APIView):
    def post(self,request):
        cleanup_inactive_users.delay()
        return cr.success(message="Manual cleanup triggered successfully.")