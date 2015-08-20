from django.conf.urls import patterns, urls

urlpatterns = patterns('djangocms_dataset_requests.views',
    url(r'^(?P<pk>[0-9]+)/(?P<slug>[\w.@+-]+)/$', 'request_detail', name='django_dataset_requests.request_detail'),
)
