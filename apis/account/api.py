from flask import request
from flask_restx import Resource

from . import app
from .model import *
from .module import *


@app.route("/register", methods=["POST"])
class Register(Resource):
    @app.expect(register_input_payload)
    @app.marshal_with(base_output_payload)
    def post(self):
        return User.register(app.payload)


@app.route("/register-check", endpoint="register-check")
class RegisterCheck(Resource):
    @app.doc(params={"uuid": "User's uuid"})
    def get(self):
        return User.register_check(request.values.get("uuid"))


@app.route("/change-password", methods=["POST"])
class ChangePassword(Resource):
    @app.expect(change_password_input_payload)
    @app.marshal_with(base_output_payload)
    def post(self):
        return User.change_password(app.payload)
