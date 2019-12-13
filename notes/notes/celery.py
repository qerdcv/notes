from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notes.settings')

app = Celery('notes', broker='redis://127.0.0.1:6379/0')

app.config_from_object('django.conf:settings', namespace='celery')

app.autodiscover_tasks()


@app.task(name="prin_one_more")
def prin_one_more():
    print('sadasasda')


@app.task(name='test_task')
def test():
    prin_one_more.delay()


app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    'print_smth': {
        'task': 'test_task',
        'schedule': timedelta(seconds=1),
    },
}
