# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'))
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)

    class Meta:
        verbose_name=_('palestrante')
        verbose_name_plural=_('palestrantes')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug})

class Contact(models.Model):
    KINDS = {
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
    }

    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)

    objects = models.Manager()
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes = KindContactManager('F')

    def __unicode__(self):
        return self.value

class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrante'))

    objects = PeriodManager()

    class Meta:
        verbose_name = _('palestra')
        verbose_name_plural = _('palestras')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/palestras/%d/' % self.pk

    @property
    def slides(self):
        return self.media_set.filter(kind='SL')

    @property
    def videos(self):
        return self.media_set.filter(kind='YT')

class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

    objects = PeriodManager()

class Media(models.Model):
    MEDIA_TYPES = (
        ('YT', _('Youtube')),
        ('SL', _('Slideshare')),
    )

    talk = models.ForeignKey('Talk')
    media_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    kind = models.CharField(max_length=2, choices=MEDIA_TYPES)

    def __unicode__(self):
        return '%s - %s' % (self.talk.title, self.title)