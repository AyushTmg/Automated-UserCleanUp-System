from django.utils import timezone
from datetime import timedelta
from .models import CleanupReport
from django.contrib.auth import get_user_model
from django.conf import settings
from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string


User = get_user_model()

@shared_task(name="cleanup_inactive_users_task")
def cleanup_inactive_users():
    threshold_date = timezone.now() - timedelta(days=int(settings.DELETE_INACTIVE_USERS_AFTER_DAYS))
    inactive_users = User.objects.filter(last_login__lt=threshold_date)
    users_deleted_count = inactive_users.count()
    
    inactive_users.delete()
    
    active_users_remaining_count = User.objects.filter(is_active=True).count()
    
    report = CleanupReport.objects.create(
        users_deleted=users_deleted_count,
        active_users_remaining=active_users_remaining_count
    )

    receipients_list = list(inactive_users.values_list('email', flat=True))
    subject = "Account Cleanup Notification"
    from_email = settings.DEFAULT_FROM_EMAIL
    context = {
        'cleanup_date': report.timestamp.strftime("%B %d, %Y, %I:%M %p"),
    }
    html_message = render_to_string('cleanup_notification/notification.html', context)

    if receipients_list:
        send_mail(
            subject=subject,
            message="", # Empty string since we're using HTML message expecting recipients have modern devices
            from_email=from_email,
            recipient_list=receipients_list,
            html_message=html_message,
            fail_silently=False,
        )
    



