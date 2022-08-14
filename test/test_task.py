from unittest.mock import patch

from . import BaseTestCase
from tasks import send_mail


class TestTask(BaseTestCase):
    def test_send_mail(self):
        title = "Register check test"
        body = "%s/apis/register-check?uuid=%s" % (
            "http://localhost:5000", "just-test")
        reciver = "davidfang147@gmail.com"

        result = send_mail.apply(kwargs={
            "title": title,
            "body": body,
            "reciver": reciver}).get()

        self.assertEqual(result, (title, body, reciver))
