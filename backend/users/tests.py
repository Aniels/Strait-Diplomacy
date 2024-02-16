from django.test import TestCase
from .models import User


class UserCreationTestCase(TestCase):
    def test_create_user(self):
        # Create a user
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Check if the user was created successfully
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))


from graphene.test import Client
from .schema import user_schema

class UserGraphQLTest(TestCase):
    def test_user_query(self):
        # Arrange
        client = Client(user_schema)

        # Act
        executed = client.execute('''
            query {
                user(id: 1) {
                    id
                    username
                    email
                }
            }
        ''')

        # Assert
        expected_data = {
            "user": {
                "id": "1",
                "username": "your_username",
                "email": "your@email.com",
            }
        }
        self.assertEqual(executed['data'], expected_data)
