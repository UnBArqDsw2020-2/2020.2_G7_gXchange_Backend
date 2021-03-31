from django.urls import path
from app.views import *

urlpatterns = [
    path("user", CreateUser.as_view(), name="user"),
]
