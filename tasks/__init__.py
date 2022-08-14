from base_api.celery import app as celery_app
from .mail import *


send_mail = celery_app.register_task(SendMail())
