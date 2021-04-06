from django.urls import path
from app.views import CreateUser

urlpatterns = [
    path("user", CreateUser.as_view(), name="user"),
]
