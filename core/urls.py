from django.urls import path
from .views.home import home
from .views.about import about
from .views.register import register

app_label = "core"

urlpatterns = [
    path("", home, name="my-home-view"),
    path("about", about, name="about-page"),
    path("register", register, name="register-page"),
]
