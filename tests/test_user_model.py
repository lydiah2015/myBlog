from app.models import User
from unittest import TestCase
from app import db

class TestUserModel(TestCase):
    def setUp(self):
        self.user=User(username="test-user",email="test-user@mail.com",passwd="password")

    def tearDown(self):
        pass

    def test_instance(self):
        self.assertIsInstance(self.user,User)

    def test_verifypassword(self):
        self.assertTrue(self.user.verifypass("password"))
        