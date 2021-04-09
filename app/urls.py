from django.urls import path
from app.views import CreateUser, UpdateUser

urlpatterns = [
    path("user", CreateUser.as_view(), name="user"),
    path("user/<str:nickname>", UpdateUser.as_view(), name="user/update")
]
