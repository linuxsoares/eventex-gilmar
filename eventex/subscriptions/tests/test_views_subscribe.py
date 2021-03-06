"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.http import response

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class SubscribeTest(TestCase):

    def setUp(self):
        #self.resp = self.client.get("/inscricao/")
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get(self):
        'GET /inscricao/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        'Html must contain input controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 7)
        self.assertContains(self.resp, 'type="text"', 5)
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'HTML must contain csrf token'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Gilmar Soares', cpf='12345678902', email='outro.soares@gmail.com', phone='11-980925399')
        #self.resp = self.client.post('/inscricao/', data)
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Valid POST'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Valid POST'
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Gilmar Soares', cpf='123456789021', email='outro.soares@gmail.com', phone='11-980925399')
        #self.resp = self.client.post('/inscricao/', data)
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Invalid POST'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Form'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())

class TemplateRegrationTest(TestCase):
    def test_template_has_non_field_errors(self):
        'Check if non_field_errors are shown in template'
        invalid_data = dict(name='Gilmar Soares', cpf='12323412303')
        response = self.client.post(r('subscriptions:subscribe'), invalid_data)

        self.assertContains(response, '<ul class="errorlist">')
