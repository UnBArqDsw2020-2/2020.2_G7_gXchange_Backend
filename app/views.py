from app.utils import base64ToBinary
from app.models import Person, Picture, Offer, User
from app.serializers import OfferSerializer, PersonSerializer
from rest_framework import generics
from rest_framework.response import Response


class CreateUser(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = "email"


class UpdateUser(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = "nickname"


class ListCreateOffer(generics.ListCreateAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = "id"

    def post(self, request):
        data = request.data

        # the back-end must find the logged user
        # leting this comment to make it easy for testing

        email = data.pop("user")

        person = Person.objects.filter(email=email)

        user = User.objects.filter(person=person[0])

        pictures = data.pop("pictures")

        # something that rhuan tell
        #user = User.objects.all()

        new_offer = Offer.objects.create(user=user[0], **data)

        for picture in pictures:
            binary_photo = base64ToBinary(picture["bin"])

            Picture.objects.create(offer=new_offer, bin=binary_photo)

        return Response(status=201)

