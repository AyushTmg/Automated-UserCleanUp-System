from django.db import models

class CleanupReport(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    users_deleted = models.IntegerField()
    active_users_remaining = models.IntegerField()

