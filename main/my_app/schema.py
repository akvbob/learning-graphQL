import graphene
import graphene_django
from my_app.models import Restaurant

class RestaurantType(graphene_django.DjangoObjectType):
  class Meta:
    model = Restaurant
    fields = ("id", "name", "address")


class Query(graphene.ObjectType):
  """
  Queries for the Restaurant model
  """
  restaurants = graphene.List(RestaurantType)

  def resolve_restaurants(self, info, **kwargs):
    return Restaurant.objects.all()
  

schema = graphene.Schema(query=Query)