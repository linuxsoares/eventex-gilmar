# coding: utf-8

from django.test import TestCase
from eventex.core.models import Talk

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da Palestra',
            start_time='10:00')

    def test_create(self):
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))

    def test_speakers(self):
        self.talk.speakers.create(name='Gilmar Soares',
                                  slug='gilmar-soares',
                                  url='http://about.me/gilmar.soares')
        self.assertEqual(1, self.talk.speakers.count())