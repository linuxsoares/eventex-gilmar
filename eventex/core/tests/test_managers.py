# coding: utf-8

from django.test import TestCase
from eventex.core.models import Contact, Speaker, Talk

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Gilmar Soares',
                                   slug='gilmar-soares', url='http://about.me/gilmar.soares')

        s.contact_set.add(Contact(kind='E', value='gilmar@soares.com'),
                          Contact(kind='P', value='11-34445654'),
                          Contact(kind='F', value='11-75864648'))

    def test_emails(self):
        qs = Contact.emails.all()
        expected = ['<Contact: gilmar@soares.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        qs = Contact.phones.all()
        expected = ['<Contact: 11-34445654>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        qs = Contact.faxes.all()
        expected = ['<Contact: 11-75864648>']
        self.assertQuerysetEqual(qs, expected)

class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='12:00')

    def test_morning(self):
        self.assertQuerysetEqual(Talk.objects.at_morning(), ['Morning Talk'], lambda t: t.title)

    def test_afternoon(self):
        self.assertQuerysetEqual(Talk.objects.at_afternoon(), ['Afternoon Talk'], lambda t: t.title)
