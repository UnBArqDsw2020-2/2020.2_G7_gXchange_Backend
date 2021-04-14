from django.urls import path
from app.views import CreateUser, CreateOffer

urlpatterns = [
    path("user", CreateUser.as_view(), name="user"),
    path("offer", CreateOffer.as_view(), name="offer"),
]
