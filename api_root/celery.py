from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_root.settings')

app = Celery('api_root')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
