from rest_framework_api_key.models import APIKey
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser

class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        data = {'email': 'mauro@gmail.com', 'first_name': 'Mauro', 'last_name': 'Lopez'}
        response = self.client.post('/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data['key'])
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertIsNotNone(CustomUser.objects.get(email='mauro@gmail.com').api_key)
        api_key = APIKey.objects.get_from_key(response.data['key'])
        user = CustomUser.objects.get(api_key=api_key)
        self.assertEqual(CustomUser.objects.get(email='mauro@gmail.com'), user)
