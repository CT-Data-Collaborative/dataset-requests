# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
# from cms.models.pluginmodel import CMSPlugin
from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey
from trello import TrelloClient


# class DatasetRequestPlugin(CMSPlugin):
#     trello_api = models.CharField(max_length=32)
#     trello_app_token = models.CharField(max_length=64)
#     trello_board = models.CharField(max_length=64)
#     label_name = models.CharField(max_length=64)
#
#     def __unicode__(self):
#         return unicode(self.pk)


class Source(Sortable):
    class Meta(Sortable.Meta):
        verbose_name_plural = 'Source'

    source_name = models.CharField(max_length=128)

    def __unicode__(self):
        return unicode(self.source_name)


class DatasetRequest(Sortable):
    '''Docstring for DatasetRequest model

    Model for holding information about data requests.
    Has two special methods that handle integration with Trello

    save_to_trello and delete_from_trello

    At some point I will want to create an inheritable class
    that contains trello api methods and which can be inherrited
    '''
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
    trello_id = models.CharField(max_length=32)

    def __unicode__(self):
        return u'%s' %(self.dataset_name)

    def save_to_trello(self):
        # print clean_form_data
        api_key = settings.TRELLO_KEY
        secret = settings.TRELLO_SECRET
        token = settings.TRELLO_TOKEN
        board = settings.TRELLO_REQUEST_BOARD

        c = TrelloClient(api_key, secret, token)
        b = c.get_board(board)
        print "Got Board"

        # Currently we default to adding card to first list
        l = b.all_lists()[0]
        print "Got List"
        label_list = b.get_labels()
        print "Got Labels"

        ds_name = "%s - %s" % (self.dataset_name, self.dataset_source)

        ds_description = "%s\n%s\nRequested by: %s %s, %s" % \
            (self.dataset_name,
            self.dataset_description,
            self.user_first_name,
            self.user_last_name,
            self.user_email)

        try:
            label_to_add = next(x for x in label_list if x.name == 'Request')
        except StopIteration:
            label_to_add = b.add_label('Request', "lime")

        try:
            card = l.add_card(ds_name, ds_description, [label_to_add])
            self.trello_id = card.id
        except Exception:
            pass

    def delete_from_trello(self):
        api_key = settings.TRELLO_KEY
        secret = settings.TRELLO_SECRET
        token = settings.TRELLO_TOKEN
        id = self.trello_id
        c = TrelloClient(api_key, secret, token)
        # b = c.get_board(board)
        card = c.get_card(id)
        try:
            card.set_closed(True)
        except Exception:
            pass

    def save(self, *args, **kwargs):
        try:
            card_id = self.save_to_trello()
            # self.trello_id = card_id
        except Exception:
            self.trello_id = ''
        super(DatasetRequest, self).save(*args, **kwargs)

    def delete(self):
        try:
            self.delete_from_trello()
            print "delete call made"
        except Exception:
            pass
        super(DatasetRequest, self).delete()

    class Meta:
        ordering = ['-created_date']
