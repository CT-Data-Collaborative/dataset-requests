# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.views.decorators.cache import never_cache

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .views import DatasetRequestView
from .models import DatasetRequestPlugin
from .forms import RequestForm

class DatasetRequestCMSPlugin(CMSPluginBase):
    cache = False
    model = DatasetRequestPlugin
    name = "Dataset Request"
    module = "Dataset Management"
    render_template = 'djangocms_dataset_requests/dataset_request.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        context['form'] = RequestForm(initial={'plugin.id': instance.pk,
                                               'redirect_url': request.get_full_path()})
        return context

    def get_request_view(self):
        return DatasetRequestView.as_view()

    def get_plugin_urls(self):
        request_view = self.get_request_view()

        return patterns('',
            url(r'^dataset-request/$', never_cache(request_view), name='dataset-request'))

plugin_pool.register_plugin(DatasetRequestCMSPlugin)
