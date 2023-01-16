from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View


class HomeView(View):
    """Provides get functionality for the home page"""
    template_name = "core/home.html"

    def get(self, request, **kwargs):
        return render(request, self.template_name, {"name": "Kalenshi Katebe"})
