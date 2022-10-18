from . import views
from django.urls import path

urlpatterns = [
    path("", views.hello, name="hello"),
    # path("<str:name>", views.greet, name="greet"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("resetpwd", views.resetpwd, name="resetpwd")
]
