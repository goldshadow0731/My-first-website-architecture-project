from uuid import uuid5, NAMESPACE_X500

from werkzeug.security import generate_password_hash, check_password_hash

from base_api.db import db


class UserProfile(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    verified = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        user_uuid = uuid5(NAMESPACE_X500, kwargs.get("name"))
        super().__init__(uuid=user_uuid, **kwargs)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
