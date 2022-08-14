from flask import Flask
from flask_mail import Mail

from DB import db


app = Flask(__name__, root_path=".")
app.config.from_pyfile('configs/pg_const.py')

db.init_app(app)

mail_app = Mail(app)
