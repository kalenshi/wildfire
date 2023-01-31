from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse, resolve

from core.views.about import about


class TestAboutPage(TestCase):
    """Tests the about page"""

    def setUp(self) -> None:
        self.view = about

    def test_about_page_uses_right_view_function(self):
        found = resolve("/about")
        self.assertEqual(found.func, about)

    def test_about_page_uses_right_template(self):
        response = self.client.get("/about")
        self.assertTemplateUsed(response, "core/about.html")

