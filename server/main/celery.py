import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from dotenv import load_dotenv
load_dotenv()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'Task One': {
        'task': 'cleanup_inactive_users_task',
        'schedule': crontab(minute=f'*/{settings.JOB_RUN_INTERVAL_MINUTES}'),  
    },
}