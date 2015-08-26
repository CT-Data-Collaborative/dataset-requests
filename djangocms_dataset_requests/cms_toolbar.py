# -*- coding: utf-8 -*-
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

@toolbar_pool.register
class DatasetRequestToolbar(CMSToolbar):

    def populate(self):
        admin_menu = self.toolbar.get_or_create_menu('djangocms_dataset_requests', _('Dataset Requests'))

    def post_template_populate(self):
        pass
