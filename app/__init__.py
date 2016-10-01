from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
#init
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


from app.views import deepsearch_view, chargestate_view, intensity_view
