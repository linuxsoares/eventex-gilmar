# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        'Form must have 4 fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'CPF must only accept digits'
        form = self.make_validated_form(cpf='A2343445454')

        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'CPF must have 11 digits'
        form = self.make_validated_form(cpf='1234')

        self.assertItemsEqual(['cpf'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Gilmar Soares', email='linux.soares@gmail.com',
                    cpf='12345678901', phone_0='11', phone_1='80915395')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def test_email_is_optional(self):
        'Email is optional'
        form = self.make_validated_form(email='')

        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        'Test Email or Phone'
        form = self.make_validated_form(email='', phone_0='', phone_1='')

        self.assertItemsEqual(['__all__'], form.errors)

    def test_name_must_be_capitalized(self):
        'Name must be capitalized'
        form = self.make_validated_form(name='GILMAR Soares')

        self.assertEqual('Gilmar Soares', form.cleaned_data['name'])




