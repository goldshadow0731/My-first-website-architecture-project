from flask_restx import fields

from . import app


base_output_payload = app.model("基本輸出", {
    "status": fields.Integer(required=True, default=0),
    "message": fields.String(required=True, default="")
})

register_input_payload = app.model("註冊輸入", {
    "username": fields.String(required=True),
    "email": fields.String(required=True),
    "password": fields.String(required=True)
})

change_password_input_payload = app.model("修改密碼輸入", {
    "username": fields.String(required=True),
    "old_password": fields.String(required=True),
    "new_password": fields.String(required=True)
})
