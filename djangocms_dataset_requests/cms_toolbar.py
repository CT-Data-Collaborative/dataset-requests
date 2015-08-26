# -*- coding: utf-8 -*-
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

@toolbar_pool.register
class DatasetRequestToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu('djangocms_dataset_requests', _('Dataset Requests'))
        url = reverse('admin:djangocms_dataset_requests_datasetrequest_changelist')
        admin_menu.add_sideframe_item(_('Dataset Requests Overview'), url=url)
        url = reverse('admin:djangocms_dataset_requests_datasetrequest_add')
        admin_menu.add_sideframe_item(_('Add Requests'), url=url)
        url = reverse('admin:djangocms_dataset_requests_source_add')
        admin_menu.add_sideframe_item(_('Add Source'), url=url)

    def post_template_populate(self):
        pass
