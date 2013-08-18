# coding: utf-8

from django.contrib.auth import get_user_model
from django.test import TestCase
from eventex.myauth.backends import EmailBackend

class EmailBackendTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='gilmar',
                                      email='gilmar@soares.net',
                                      password='gilmar')
        self.backend = EmailBackend()

    def test_authenticate_with_email(self):
        user = self.backend.authenticate(email='gilmar@soares.net',
                                         password='wrong')
        self.assertIsNone(user)

    def test_unknown_user(self):
        user = self.backend.authenticate(email='teste@soares.net',
                                         password='gilmar')
        self.assertIsNone(user)

    def test_get_user(self):
        self.assertIsNotNone(self.backend.get_user(1))

class MultipleEmailsTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        UserModel.objects.create_user(username='user1',
                                      email='gilmar@soares.net',
                                      password='gilmar')
        UserModel.objects.create_user(username='user1',
                                      email='gilmar@soares.net',
                                      password='gilmar')

# class FunctionalEmailBackendTest(TestCase):
#     def setUp(self):
#         UserModel = get_user_model()
#         UserModel.objects.create_user(username='gilmar',
#                                       email='gilmar@soares.net',
#                                       password='gilmar')
#
#     def test_login_with_email(self):
#         result = self.client.login(email='gilmar@soares.net',
#                                  password='gilmar')
#         self.assertTrue(result)
#
#     def test_login_with_user(self):
#             result = self.client.login(username='gilmar@soares.net',
#                                      password='gilmar')
#             self.assertTrue(result)