from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpass")

    def test_user_registration(self):
        #Test user can register#
        response = self.client.post('/users/register/', {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        #Test user can log in#
        self.client.login(username="testuser", password="testpass")
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        #Test user can log out#
        self.client.login(username="testuser", password="testpass")
        self.client.get('/users/logout/')
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)