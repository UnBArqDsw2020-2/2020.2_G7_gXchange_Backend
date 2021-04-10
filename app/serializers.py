from rest_framework import serializers
from app.models import Person, User, Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ["phone_number"]


class PersonSerializer(serializers.ModelSerializer):
    phones = PhoneSerializer(many=True)

    def create(self, validated_data):
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
