# coding: utf-8
__author__ = 'gilmar'

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Gilmar Soares', cpf='123456789021', email='outro.soares@gmail.com', phone='11-980925399')
        #self.resp = self.client.get('/inscricao/%d/' % s.pk)
        self.resp = self.client.get(r('subscriptions:detail', args=[s.pk]))

    def test_get(self):
        'GET'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses Template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check HTML'
        self.assertContains(self.resp, 'Gilmar Soares')

class DetailNotFound(TestCase):
    def test_not_found(self):
        #response = self.client.get('/inscricao/0/')
        response = self.client.get(r('subscriptions:detail', args=[0]))
        self.assertEqual(404, response.status_code)
