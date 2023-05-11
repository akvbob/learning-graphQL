from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
  path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
] # that will automatically open the GraphiQL API browser for testing our queries and mutations.