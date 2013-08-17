# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk

class TalkListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name='Gilmar Soares', slug='gilmar-soares',
                                   url='http://about.me/gilmar.soares', description='Passionate software developer!')
        t1 = Talk.objects.create(description=u'Descrição da Palestra',
                                 title=u'Título da Palestra', start_time='10:00')
        t2 = Talk.objects.create(description=u'Descrição da Palestra',
                                 title=u'Título da Palestra', start_time='13:00')
        t1.speakers.add(s)
        t2.speakers.add(s)
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        self.assertContains(self.resp, u'Título da Palestra', 2)
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/gilmar-soares/', 2)
        self.assertContains(self.resp, u'Passionate software developer!', 2)
        self.assertContains(self.resp, u'Gilmar Soares', 2)
        self.assertContains(self.resp, u'Descrição da Palestra', 2)