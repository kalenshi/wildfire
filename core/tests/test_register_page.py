from django.test import TestCase
from django.urls import resolve

from core.views.register import register


class TestRegisterPage(TestCase):
    """Test user can register usng email"""

    def setUp(self) -> None:
        self.view = register

    def test_register_page_uses_right_template(self) -> None:
        response = self.client.get("core:register-page")
        self.assertTemplateUsed(response, "core/register.html")
