from django.test import TestCase
from unittest.mock import patch


# NOTE: This inherits from the Django TestCase class
class TestUserInfo(TestCase):

    # NOTE: fixtures are loaded automatically by Django
    fixtures = ['users/fixtures/user-data']

    def setUp(self):
       pass

    def tearDown(self):
        pass

    @patch("example3.users.views.TAS")
    def test_get_user_info(self, mock_tas):
        mock_tas().getUserInfo.return_value = {
            "full_name": "Test User"
        }
        resp = self.client.get("/users/info/1/")
        self.assertTrue(resp.status_code == 200)
        data = resp.json()
        print(resp)
        print(dir(resp))
        self.assertTrue(data["full_name"] == "Test User")