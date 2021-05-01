from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import validate_unicode_slug
from django.utils.translation import gettext as _
from django.contrib.auth.models import UserManager


class Person(AbstractBaseUser):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, primary_key=True)
    nickname = models.CharField(max_length=256, unique=True, validators=[validate_unicode_slug])
    picture = models.BinaryField()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
        "password",
    ]
    objects = UserManager()


class Phone(models.Model):
    person = models.ForeignKey(Person, related_name="phones", on_delete=models.CASCADE)
    phone_number = models.BigIntegerField()


class User(models.Model):
    person = models.OneToOneField(Person, primary_key=True, on_delete=models.CASCADE)
    ratings_amount = models.IntegerField(default=0, null=True)
    sells_amount = models.IntegerField(default=0, null=True)
    average = models.DecimalField(max_digits=3, decimal_places=2, null=True)


class ZipCode(models.Model):
    email = models.ForeignKey(Person, on_delete=models.CASCADE)
    cep = models.CharField(max_length=50)


class Offer(models.Model):
    class ConditionEnum(models.IntegerChoices):
        NEW = 1, _("New")
        SEMINEW = 2, _("Seminew")
        USED = 3, _("Used")

    game_name = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    description = models.TextField(null=True)
    is_valid = models.BooleanField(default=True)
    is_trade = models.BooleanField(default=True)
    cep = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    condition = models.IntegerField(choices=ConditionEnum.choices)
    user = models.ForeignKey(User, related_name="offers", on_delete=models.CASCADE)


class Picture(models.Model):
    bin = models.BinaryField()
    offer = models.ForeignKey(Offer, related_name="pictures", on_delete=models.CASCADE)
