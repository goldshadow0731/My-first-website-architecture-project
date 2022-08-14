from flask_testing import TestCase
from unittest.mock import patch

import pytest

from app import app, db
from base_api.celery import app as celery_app
from configs import *


pytest_plugins = ('celery.contrib.pytest', )


@pytest.mark.usefixtures('celery_session_app')
@pytest.mark.usefixtures('celery_session_worker')
class BaseTestCase(TestCase):
    username = "admin"
    email = "davidfang147@gmail.com"
    password = "admin"

    def create_app(self):
        app.config["TESTING"] = True
        celery_app.conf.update(CELERY_ALWAYS_EAGER=True)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    @patch('tasks.send_mail.delay')
    def signup(self, function_mock, username=None, email=None, password=None):
        response = self.client.post("/api/account/register",
                                    json={
                                        "username": username if username is not None else self.username,
                                        "email": email if email is not None else self.email,
                                        "password": password if password is not None else self.password
                                    })
        if response.json.get("status") == 0:
            function_mock.assert_called()
        return response
