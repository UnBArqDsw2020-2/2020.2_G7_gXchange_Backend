from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Person(AbstractBaseUser):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, primary_key=True)
    nickname = models.CharField(max_length=256, unique=True)
    picture = models.BinaryField()
    USERNAME_FIELD = "nickname"
    REQUIRED_FIELDS = [
        "name",
        "email",
        "password",
    ]


class Phone(models.Model):
    email = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.IntegerField()


class User(models.Model):
    email = models.ForeignKey(Person, on_delete=models.CASCADE)
    ratings_amount = models.IntegerField(default=0)
    sells_amount = models.IntegerField(default=0)
    average = models.DecimalField(max_digits=3, decimal_places=2)


class ZipCode(models.Model):
    email = models.ForeignKey(Person, on_delete=models.CASCADE)
    cep = models.CharField(max_length=50)


class Offer(models.Model):
    class ConditionEnum(models.IntegerChoices):
        NEW = 1, _("New")
        SEMINEW = 2, _("Seminew")
        USED = 3, _("Used")

    game_name = models.CharField(max_length=200)
    plataform = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_valid = models.BooleanField(default=True)
    date = models.DateField()
    cep = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    condition = models.IntegerField(choices=ConditionEnum.choices)
    email = models.ForeignKey(Person, on_delete=models.CASCADE)


class Picture(models.Model):
    bin = models.BinaryField()
    id_offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
