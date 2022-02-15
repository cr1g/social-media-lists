from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


class CustomAPIClient(APIClient):
    """
    Custom APIClient that overrides some of its default behavior.
    """

    def get(self, path, data=None, follow=False, auth=None, **extra):
        if auth:
            extra['HTTP_AUTHORIZATION'] = f'Bearer {auth}'

        return super().get(path, data=data, **extra)

    def post(self, path, data=None, format='json', auth=None,
             content_type=None, follow=False, **extra):
        if auth:
            extra['HTTP_AUTHORIZATION'] = f'Bearer {auth}'

        return super().post(
            path, data=data, format=format,
            content_type=content_type, **extra
        )

    def put(self, path, data=None, format='json', auth=None,
            content_type=None, follow=False, **extra):
        if auth:
            extra['HTTP_AUTHORIZATION'] = f'Bearer {auth}'

        return super().put(
            path, data=data, format=format,
            content_type=content_type, **extra
        )

    def delete(self, path, data=None, format=None, auth=None,
               content_type=None, follow=False, **extra):
        if auth:
            extra['HTTP_AUTHORIZATION'] = f'Bearer {auth}'

        return super().delete(
            path, data=data, format=format,
            content_type=content_type, **extra
        )


class CustomTestCase(TestCase):
    """
    Custom TestCase that initializes a CustomAPIClient by default.
    """

    def setUp(self):
        self.client = CustomAPIClient()
        
        User.objects.create_superuser(
            'admin', 'admin@b4y.com', 'complexpassword'
        )
