# coding: utf-8

__author__ = 'gilmar'

from  django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name="Gilmar Soares",
            cpf="12345678902",
            email="linux.soares@gmail.com",
            phone="11-980915395"
        )
    def test_create(self):
        'Subscription must have name, cpf, email e phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Gilmar Soares', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        #Create a first entry to force the colision
        Subscription.objects.create(name='Gilmar Soares', cpf='12345678902', email='linux.soares@gmail.com', phone='11-980925399')

    def test_cpf_unique(self):
        'Cpf must be unique'
        s = Subscription(name='Gilmar Soares', cpf='12345678902', email='outro.soares@gmail.com', phone='11-980925399')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(name='Gilmar Soares', cpf='12345678904', email='linux.soares@gmail.com', phone='11-980925399')
        self.assertRaises(IntegrityError, s.save)







