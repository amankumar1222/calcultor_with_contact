from django.urls import path , include
from .import views

urlpatterns = [
    path("", views.index, name="home"),
    path("math/", views.math_fun, name="math"),
    path("contact/", views.contact, name="math"),
]
