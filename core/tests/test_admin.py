"""
Tests the Django admin works with the changes on the user model
"""
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTest(TestCase):
    """Tests the admin site works with our User model"""

    def setUp(self) -> None:
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="test_password"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="testpass123"
        )

    def tearDown(self) -> None:
        pass

    def test_users_are_listed_on_page(self) -> None:
        """Test that all users can be viewed in the admin page"""
        url = reverse("admin:core_user_changelist")  # Gets the page that contains the list of users
        response = self.client.get(url)

        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.email)

    def test_user_edit_page(self) -> None:
        """Test user modification works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self) -> None:
        """Tests support for adding new users """
        url = reverse("admin:core_user_add")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
