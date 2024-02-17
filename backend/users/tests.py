from django.test import TestCase
from graphene.test import Client
from .schema import user_schema
from .models import User

# Define a test case for user creation
class UserCreationTestCase(TestCase):
    def test_create_user(self):
        # Create a user using Django's create_user method
        user = User.objects.create_user(username='testuser', password='testpassword')

        # Check if the user was created successfully by asserting the username and password
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))

# Define a test case for GraphQL queries and mutations
class UserGraphQLTestCase(TestCase):
    def setUp(self):
        # Set up a GraphQL client using the schema
        self.client = Client(user_schema)

    def test_create_user_mutation(self):
        # Define a GraphQL mutation for creating a user
        mutation = '''
        mutation {
            createUser(username: "testuser", password: "testpassword") {
                createdUser {
                    id
                    username
                }
            }
        }
        '''

        # Execute the mutation using the GraphQL client
        response = self.client.execute(mutation)

        # Check if the mutation was successful by asserting the response data
        self.assertIsNotNone(response['data']['createUser'])
        self.assertEqual(response['data']['createUser']['createdUser']['username'], 'testuser')

        # Check if the user was actually created in the database
        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user)

    def test_all_users_query(self):
        # Create a user for the test
        User.objects.create(username='testuser', password='testpassword')

        # Define a GraphQL query for getting all users
        query = '''
        query {
            allUsers {
                id
                username
            }
        }
        '''

        # Execute the query using the GraphQL client
        response = self.client.execute(query)

        # Check if the query was successful by asserting the response data
        self.assertIsNotNone(response['data']['allUsers'])
        self.assertEqual(len(response['data']['allUsers']), 1)
        self.assertEqual(response['data']['allUsers'][0]['username'], 'testuser')
