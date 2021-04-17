from django.urls import path
from app.views import CreateUser, UpdateUser, CreateOffer

urlpatterns = [
    path("user", CreateUser.as_view(), name="user"),
    path("user/<str:nickname>", UpdateUser.as_view(), name="user/update"),
    path("offer", CreateOffer.as_view(), name="offer"),
]
