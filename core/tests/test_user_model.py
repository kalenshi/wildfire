from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUserModel(TestCase):
    """Test the apps user model"""

    def test_can_create_user_with_email(self):
        """Test creating a user with email is successful"""
        email = "test@example@com"  # use example.com because it's specifically reserved  for testing
        password = "secure_password"

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)

        self.assertTrue(user.check_password(password))

    def test_can_not_create_user_without_email(self):
        """Tests New users must provide email"""
        with self.assertRaises(ValueError) as e:
            user = get_user_model().objects.create_user(
                email="",
                password="password123"
            )
        self.assertEqual(
            e.exception.args[0],
            "Email is a required Field for all users."
        )

    def test_normalizes_email(self):
        """Tests normalizes the email address"""
        sample_emails = [
            ("test1@EXAMPLE.com", "test1@example.com"),
            ("Test2@Example.com", "Test2@example.com"),
            ("TEST3@EXAMPLE.COM", "TEST3@example.com"),
            ("test4@example.COM", "test4@example.com"),
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(
                email=email,
                password="password123"
            )
            self.assertEqual(user.email, expected)

    def test_can_create_and_save_a_superuser(self):
        """Test superuser creation"""
        user = get_user_model().objects.create_superuser(
            email="test@example.com",
            password="test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
