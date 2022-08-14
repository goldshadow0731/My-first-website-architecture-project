from celery import Celery

from configs import *


app = Celery(__name__,
             backend=RESULT_BACKEND,
             broker=BROKER_URL)
