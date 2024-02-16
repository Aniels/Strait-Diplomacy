from django.test import TestCase
from .models import User

class UserCreationTestCase(TestCase):
    def test_create_user(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Check if the user was created successfully
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))
