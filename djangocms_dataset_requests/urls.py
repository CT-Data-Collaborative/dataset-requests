from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # URL pattern for the UserListView  # noqa
    url(r'^$', views.DatasetRequestsListView.as_view(), name='request_home'),
    url(r'^(?P<pk>[0-9]+)/$', views.DatasetRequestDetailView.as_view(), name='request_detail'),
    url(r'^new_request/$', views.DatasetRequestView.as_view(), name='new_request'),
)
