from . import views
from django.urls import path

urlpatterns = [
    path("", views.hello, name="hello"),
    path("<str:name>", views.greet, name="greet")
]
