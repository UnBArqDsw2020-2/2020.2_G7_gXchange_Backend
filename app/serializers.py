from rest_framework import serializers
from app.models import Person, User


class PersonSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        person_new = Person.objects.create(**validated_data)
        User.objects.create(person=person_new)

        return person_new

    class Meta:
        model = Person
        fields = "__all__"
