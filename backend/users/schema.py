import graphene
from graphene import InputObjectType
from graphene_django.types import DjangoObjectType
from .models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ["id", "username"]

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

class CreateUser(graphene.Mutation):
    # We need a name to create a new User instance.
    class Arguments:
        username = graphene.String()
        password = graphene.String()
    
    # The result of the mutation. It returns a field of type UserType.
    createdUser = graphene.Field(UserType)

    # The mutate method is where the magic happens. It creates a new User instance with the provided name and description,
    # saves it to the database, and then returns the result in the format specified by CreateUser.
    def mutate(self, info, username, password):
        user = User(username=username, password=password)
        user.save()

        # Return the result of the mutation. In this case, we create a CreateUser object with the new User instance.
        return CreateUser(createdUser=user)

# The Mutation class is an ObjectType that defines all the mutations available in our schema.
class Mutation(graphene.ObjectType):
    # We define a single mutation called "create_User". It uses the CreateUser mutation we defined above.
    create_User = CreateUser.Field()


user_schema = graphene.Schema(query=Query, mutation=Mutation)
