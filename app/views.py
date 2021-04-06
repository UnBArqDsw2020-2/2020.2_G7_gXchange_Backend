from app.models import Person
from app.serializers import PersonSerializer
from rest_framework import generics


class CreateUser(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = ["email"]
