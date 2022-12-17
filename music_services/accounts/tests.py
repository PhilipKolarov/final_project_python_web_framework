from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from music_services.accounts.models import AppUser


UserModel = get_user_model()


class AppUserTests(TestCase):
    def test_userCreate_whenInvalidUsername_shouldRaise(self):
        user = AppUser(
            username='Jo',
            email='jo@c.om',
            password='9Ero0jdf'
        )

        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)


    def test_userCreate_whenValidUsername_shouldCreate(self):
        user = AppUser(
            username='Jo1000',
            email='jo@c.om',
            password='9Ero0jdf',
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user)


    def test_UpdateUser_whenValidUsername_shouldUpdate(self):
        user = AppUser(
            username='Jo1000',
            email='jo@c.om',
            password='9Ero0jdf',
        )

        user.full_clean()
        user.first_name = 'Jo'
        user.save()

        self.assertIsNotNone(user.first_name)


class ViewsTests(TestCase):
    valid_user_data = {
        'username': 'Jo',
        'email': 'jo@c.om',
        'password': '9Ero0jdf',
    }

    def test_getRegisterPage_shouldRenderTemplate(self):
        response = self.client.get(reverse('register user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/account-register.html')

    def test_getLogoutPage_shouldFailIfNotLoggedIn(self, data=valid_user_data):
        UserModel.objects.create_user(**data)

        response = self.client.get(reverse('logout user'))
        self.assertEqual(response.status_code, 302)
