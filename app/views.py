from app.utils import base64ToBinary, binaryToBase64
from app.models import Person, Picture, Offer, User, Phone
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from app.serializers import OfferSerializer, PersonSerializer, UserSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from app.utils import get_logged_user


class CreateUser(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            data = request.data

            data["picture"] = base64ToBinary(data["picture"])
            data["password"] = make_password(
                data["password"],
            )
            phone_num = data.pop("phones")
            phone_num = phone_num[0]["phone_number"]

            person_new = Person.objects.create(**data)
            User.objects.create(person=person_new)
            Phone.objects.create(person=person_new, phone_number=phone_num)

            return Response(status=201)
        except:
            return Response(status=422)


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

        pictures = data.pop("pictures")

        user = get_logged_user(request)

        new_offer = Offer.objects.create(user=user, **data)

        for picture in pictures:
            binary_photo = base64ToBinary(picture["bin"])

            Picture.objects.create(offer=new_offer, bin=binary_photo)

        return Response(status=201)


class UpdateOffer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = "id"

    def update(self, request, **kwargs):
        data = request.data

        pictures = data.pop("pictures")

        offer = Offer.objects.get(id=kwargs["id"])

        Picture.objects.filter(offer_id=kwargs["id"]).delete()

        for d in data:
            offer.__dict__[d] = data[d]

        for picture in pictures:
            binary_photo = base64ToBinary(picture["bin"])
            Picture.objects.create(offer=offer, bin=binary_photo)

        offer.save()

        return Response(status=201)


class getOffers(generics.ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    lookup_field = "id"

    def get_queryset(self):
        user = get_logged_user(request)
        return Offer.objects.filter(user=user)



class PingView(APIView):
    def post(self, request):
        user = get_logged_user(request)

        if user:
            serializer = UserSerializer(user)

            person = Person.objects.get(email=serializer.data["person"]["email"])

            serializer.data["picture"] = binaryToBase64(person.picture)

            return Response(status=200, data=serializer.data)

        return Response(status=401)
