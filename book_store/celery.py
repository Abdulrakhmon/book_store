from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')
app = Celery('book_store')
app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'send_excel_every_monday_morning': {
        'task': 'books.tasks.send_excel',
        'schedule': crontab(hour=5, minute=0, day_of_week=1),
    },

}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
