from rest_framework import serializers
from app.models import Person, User, Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ["phone_number"]


class PersonSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)

    def create(self, validated_data):
        phone_num = validated_data.pop("phone")
        phone_num = phone_num["phone_number"]
        person_new = Person.objects.create(**validated_data)
        User.objects.create(person=person_new)
        Phone.objects.create(email=person_new, phone_number=phone_num)

        return person_new

    class Meta:
        model = Person
        fields = ["name", "email", "nickname", "password", "picture", "phones"]
