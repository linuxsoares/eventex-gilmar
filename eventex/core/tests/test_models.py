# coding: utf-8

from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError

class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name='Gilmar Soares',
                               slug='gilmar-soares',
                               url='http://about.me/gilmar.soares',
                               description ='Passionate software developer!')
        self.speaker.save()

    def test_create(self):
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        self.assertEqual(u'Gilmar Soares', unicode(self.speaker))

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name='Gilmar Soares',
                               slug='gilmar-soares',
                               url='http://about.me/gilmar.soares',
                               description ='Passionate software developer!')

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E', value='gilmar@soares.net')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P', value='11-89998766')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='F', value='11-12345566')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        contact = Contact(speaker=self.speaker, kind='E', value='gilmar@soares.net')
        self.assertEqual(u'gilmar@soares.net', unicode(contact))

