from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes.settings')
app = Celery('notes')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def test(arg):
    print(arg)


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'test',
        'schedule': 10.0,
        'args': 16
    },
}

app.conf.timezone = 'UTC'