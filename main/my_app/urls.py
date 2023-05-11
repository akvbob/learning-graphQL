from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from my_app.schema import schema

urlpatterns = [
  path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
] # that will automatically open the GraphiQL API browser for testing our queries and mutations.