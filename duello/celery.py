import os

from celery import Celery

app = Celery("duello")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
