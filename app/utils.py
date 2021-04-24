import jwt
import base64
from django.conf import settings
from app.models import Person, User
from rest_framework.authentication import get_authorization_header


def base64ToBinary(base64_str):
    base64_bytes = base64_str.encode("ascii")

    return base64.b64decode(base64_bytes)


def binaryToBase64(binary_data):
    base64_bytes = base64.b64encode(binary_data)

    return base64_bytes.decode("ascii")


def get_logged_user_email(request):
    token = get_authorization_header(request).decode("utf-8").replace("Bearer ", "")

    if token is None or token == "null" or token.strip() == "":
        return None

    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")

    return decoded["user_id"]


def get_logged_user(request):
    token = get_authorization_header(request).decode("utf-8").replace("Bearer ", "")

    if token is None or token == "null" or token.strip() == "":
        return None

    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")

    user_email = decoded["user_id"]

    person = Person.objects.get(email=user_email)

    return User.objects.get(person=person)
