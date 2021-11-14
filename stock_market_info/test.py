from rest_framework_api_key.models import APIKey
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser

class AccountTests(APITestCase):
    def test_get_fb_info(self):
        """
        Ensure we can create a new account object.
        """
        data = {'email': 'mauro@gmail.com', 'first_name': 'Mauro', 'last_name': 'Lopez'}
        response = self.client.post('/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        key = response.data['key']
        self.client.credentials(HTTP_AUTHORIZATION='Api-Key ' + key)
        response = self.client.get('/market/FB', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
