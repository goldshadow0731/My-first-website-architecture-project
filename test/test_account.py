from uuid import uuid5, NAMESPACE_X500

from . import BaseTestCase


class TestAccountApi(BaseTestCase):
    def test_register(self):
        # Empty
        response = self.signup(username="", email="", password="")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, {'status': 1, 'message': "Username should not be empty."})

        # Success
        response = self.signup()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 0, 'message': ""})

        # Repect
        response = self.signup()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, {'status': 1, 'message': "The username has been registered."})

    def test_register_check(self):
        self.signup()
        uuid = uuid5(NAMESPACE_X500, "admin")

        # Not found
        response = self.client.get("/api/account/register-check",
                                   query_string={
                                       "uuid": "01234567-0123-4567-8900-012345678900"
                                   })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, {'status': 1, 'message': "UUID not found."})

        # Success
        response = self.client.get("/api/account/register-check",
                                   query_string={
                                       "uuid": uuid
                                   })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 0, 'message': ""})

        # Has verified
        response = self.client.get("/api/account/register-check",
                                   query_string={
                                       "uuid": uuid
                                   })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, {'status': 1, 'message': "User has verified."})

    def test_change_password(self):
        self.signup()

        self.client.get("/api/account/register-check",
                        query_string={
                            "uuid": uuid5(NAMESPACE_X500, "admin")
                        })

        # Success
        response = self.client.post("/api/account/change-password",
                                    json={
                                        "username": "admin",
                                        "old_password": "admin",
                                        "new_password": "root"
                                    })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 0, 'message': ""})

        # Wrong
        response = self.client.post("/api/account/change-password",
                                    json={
                                        "username": "admin",
                                        "old_password": "admin",
                                        "new_password": "root"
                                    })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, {'status': 1, 'message': "password error"})
