from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("conrad", views.conrad, name="conrad"),
    path("silas", views.silas, name="silas"),
    path("<str:name>", views.greet, name="greet")
]