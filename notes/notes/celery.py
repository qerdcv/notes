from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes.settings')

app = Celery('notes', broker='redis://notes_redis:6379/0')

app.config_from_object('django.conf:settings', namespace='celery')

app.autodiscover_tasks()

app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'delete_notes': {
        'task': 'remove_done_notes',
        'schedule': crontab(minute=0, hour=0)
    }
}
