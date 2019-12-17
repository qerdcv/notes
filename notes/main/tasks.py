from celery.decorators import task
from .models import Notes


@task(name='remove_done_notes')
def remove_done_notes():
    Notes.objects.filter(is_done=True).delete()
    return 'DONE NOTES WAS DELETED'