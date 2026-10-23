from celery import Celery
import os

#celery Configurations

os.environ.setdefault("DJANGO_SETTINGs_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()