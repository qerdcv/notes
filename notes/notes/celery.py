from __future__ import absolute_import

import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes.settings')
app = Celery(__name__, backend='redis://localhost', broker='redis:'
                                                           '//')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(name="prin_one_more")
def prin_one_more():
    print('sadasasda')


@app.task(name='test_task')
def test():
    prin_one_more.delay()


app.conf.timezone = 'UTC'

CELERY_BEAT_SCHEDULE = {
    'print_smth': {
        'task': 'test_task',
        'schedule': crontab(),
    },
}