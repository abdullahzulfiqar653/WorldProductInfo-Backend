from django.test import TestCase
from django.contrib.auth.models import User

class UserCreateTestCase(TestCase):
    def testUserCreate(self):
        user = User(username="abdul", email="testing@abdullahzulfiqar.me", password="haha@123")
        self.assertEqual(user.username, "abdul")
        self.assertEqual(user.email, "testing@abdullahzulfiqar.me")
