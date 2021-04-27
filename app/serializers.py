from rest_framework import serializers
from rest_framework.serializers import CharField
from app.models import Person, User, Offer, Picture, Phone
from django.contrib.auth.hashers import make_password


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ["phone_number"]


class PersonSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)

    def create(self, validated_data):
        validated_data["password"] = make_password(
            validated_data["password"],
        )
        phone_num = validated_data.pop("phones")
        phone_num = phone_num[0]["phone_number"]
        person_new = Person.objects.create(**validated_data)
        User.objects.create(person=person_new)
        Phone.objects.create(person=person_new, phone_number=phone_num)

        return person_new

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.nickname = validated_data["nickname"]
        phone = instance.phones.all()[0]
        phone.phone_number = validated_data["phones"][0]["phone_number"]
        phone.save()
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ["name", "email", "nickname", "password", "picture", "phones"]


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
            "id",
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
