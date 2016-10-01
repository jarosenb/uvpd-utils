import os

SECRET_KEY = 'top-secret!'

CELERY_BROKER_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = 'db+' + os.getenv('DATABASE_URL', 'postgresql://localhost/flask_sandbox')
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

SQLALCHEMY_TRACK_MODIFICATIONS = False


