from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View


def home(request) -> None:
    """function view of the home page"""
    return render(
        request,
        "core/home.html",
        {"name": "Man Kalenshi", "is_authenticated": False}
    )
