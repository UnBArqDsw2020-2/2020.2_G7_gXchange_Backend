from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Person(AbstractBaseUser):
    name = models.CharField(max_length=256)
    email = models.EmailField(
        max_length=256,
        primary_key=True
    )
    nickname = models.CharField(
        max_length=256,
        unique=True
    )
    picture = models.BinaryField()
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = [
        'name',
        'email',
        'password',
    ]


class Phone(models.Model):
    email = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    phone_number = models.IntegerField()


class User(models.Model):
    email = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    ratings_amount = models.IntegerField(default=0)
    sells_amount = models.IntegerField(default=0)
    average = models.DecimalField(max_digits=3, decimal_places=2)


class ZipCode(models.Model):
    email = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    cep = models.CharField(max_length=50)
