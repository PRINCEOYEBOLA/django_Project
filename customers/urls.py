from django.urls import path
from .views import customers, register, signin

app_name = "customers"

urlpatterns = [
    path("", customers, name = "customersView"), 
    path("register/", register, name = "registerView"),
    path("signin/", signin, name = "signinView"),
]