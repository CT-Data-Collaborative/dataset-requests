# -*- coding: utf-8 -*-
from django.db import models

from cms.models.pluginmodel import CMSPlugin
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey

class DatasetRequestPlugin(CMSPlugin):
    trello_api = models.CharField(max_length=32)
    trello_app_token = models.CharField(max_length=64)
    trello_board = models.CharField(max_length=64)
    label_name = models.CharField(max_length=64)

    def __unicode__(self):
        return unicode(self.pk)


class Source(Sortable):
    class Meta(Sortable.Meta):
        verbose_name_plural = 'Source'

    source_name = models.CharField(max_length=128)

    def __unicode__(self):
        return unicode(self.source_name)


class DatasetRequest(Sortable):
    class Meta(object):
        verbose_name_plural = 'Dataset Requests'

    PENDING = 'PN'
    OPEN = 'OP'
    CLOSED = 'CL'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
        (REJECTED, 'Rejected')
    )
    dataset_name = models.CharField(max_length=40)
    dataset_description = models.CharField(max_length=40)
    dataset_source = SortableForeignKey(Source)
    user_first_name = models.CharField(max_length=40)
    user_last_name = models.CharField(max_length=40)
    user_email = models.EmailField()
    user_notified = models.BooleanField(default=False)
    status = models.CharField(max_length=2,
                                      choices=STATUS_CHOICES,
                                      default=PENDING)
    created_date = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return u'%s' %(self.dataset_name)

    class Meta:
        ordering = ['-created_date']
