
Below is an API endpoint document for the provided GraphQL schema. This document outlines the available queries and mutations for managing users using the `user_schema`.

## User Schema API Documentation

### Query: Get All Users
- **Endpoint**: `/graphql`
- **Method**: `POST`
- **Query**:
    ```graphql
    query {
        all_users {
            id
            username
        }
    }
    ```
- **Description**: Retrieves a list of all users from the database.

### Mutation: Create User
- **Endpoint**: `/graphql`
- **Method**: `POST`
- **Mutation**:
    ```graphql
    mutation {
        create_User(username: "example_user", password: "secure_password") {
            createdUser {
                id
                username
            }
        }
    }
    ```
- **Description**: Creates a new user with the provided `username` and `password`.

### Example Usage
1. To retrieve all users, make a `POST` request to `/graphql` with the query:
    ```graphql
    query {
        all_users {
            id
            username
        }
    }
    ```
2. To create a new user, make a `POST` request to `/graphql` with the mutation:
    ```graphql
    mutation {
        create_User(username: "new_user", password: "secret_password") {
            createdUser {
                id
                username
            }
        }
    }
    ```

