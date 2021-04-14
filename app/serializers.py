from rest_framework import serializers
from rest_framework.serializers import CharField
from app.models import Person, User, Offer, Picture


class PersonSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        person_new = Person.objects.create(**validated_data)
        User.objects.create(person=person_new)

        return person_new

    class Meta:
        model = Person
        fields = "__all__"


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ["bin"]


class OfferSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, required=False)
    user = CharField()

    class Meta:
        model = Offer
        fields = [
            "offer_id",
            "game_name",
            "plataform",
            "price",
            "description",
            "is_trade",
            "cep",
            "condition",
            "user",
            "pictures",
        ]
