from django.urls import path
from app.views import CreateUser, UpdateUser, CreateOffer, UpdateOffer
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("user", CreateUser.as_view(), name="user"),
    path("user/<str:nickname>", UpdateUser.as_view(), name="user/update"),
    path("offer", CreateOffer.as_view(), name="offer"),
    path("offer/<int:id>", UpdateOffer.as_view(), name="offer/update"),
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
