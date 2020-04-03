from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # test creating a new user with an email is successful
        email = 'sohail21400@gmail.com'
        password = 'Testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normailzed(self):
        # in emails the second part will never be uppercase
        # so even if user enters with upercase we need to convert it lower

        # test the email for a new user is normalized
        email = 'sohail21400@GMAIL.COM'
        user = get_user_model().objects.create_user(email, "test1234")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # tests creating user with no email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_super_user(self):
        # test creating new super user
        user = get_user_model().objects.create_superuser(
            'sohail21400@gmail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
