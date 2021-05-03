from rest_framework import serializers
from app.models import Person, User, Offer, Picture, Phone
from app.utils import binaryToBase64


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ["phone_number"]


class PersonSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)

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
        extra_kwargs = {"password": {"write_only": True}}


class UserSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = User
        fields = ["ratings_amount", "sells_amount", "average", "person"]


class UserResumeField(serializers.RelatedField):
    def to_representation(self, value):
        phone_num = Phone.objects.filter(person=value.person)[0].phone_number

        return {
            "phone": phone_num,
            "average": value.average,
            "name": value.person.name,
            "ratings_amount": value.ratings_amount,
            "sells_amount": value.sells_amount,
            "picture": binaryToBase64(value.person.picture),
        }


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ["bin"]


class OfferSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, required=False)
    user = UserResumeField(read_only=True)

    class Meta:
        model = Offer
        fields = [
            "id",
            "game_name",
            "platform",
            "price",
            "description",
            "is_trade",
            "cep",
            "condition",
            "user",
            "pictures",
        ]
