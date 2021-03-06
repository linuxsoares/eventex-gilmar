# coding: utf-8

from django.contrib import admin
from eventex.subscriptions.models import Subscription
from django.utils.datetime_safe import datetime
from django.utils.translation import ungettext, ugettext as _, ugettext


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    list_filter = ['created_at']

    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.today().date()

    subscribed_today.short_description = _(u'Inscrito Hoje?')
    subscribed_today.boolean = True

    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        msg = ungettext(
            u'%d inscrição foi marcada como paga com sucesso.',
            u'%d foram marcadas como pagas com sucesso.',
            count
        )
        self.message_user(request, msg % count)

    mark_as_paid.short_description = _('Marcar como Pago')

admin.site.register(Subscription, SubscriptionAdmin)
