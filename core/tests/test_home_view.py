from django.test import TestCase
from core.views.home import HomeView


class TestHomeView(TestCase):
    """Test the home view and it's functionality"""

    def setUp(self) -> None:
        self.view = HomeView.as_view()

    def test_home_view_uses_the_right_template(self) -> None:
        """Test the home view is using the correct template"""
        response = self.client.get("/")

        self.assertTemplateUsed(response, "core/home.html")
