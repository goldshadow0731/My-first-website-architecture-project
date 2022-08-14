from flask import Blueprint
from flask_restx import Api

from .account.api import app as account_ns


api_bp = Blueprint("APIs", __name__, url_prefix="/api")

api = Api(api_bp, title="My first web architecture demo", doc="/doc")
api.add_namespace(account_ns)
