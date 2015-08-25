from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('djangocms_dataset_requests.view',
    # URL pattern for the UserListView  # noqa
    url(r'^$', RequestsHomeView, name='request_home'),
    url(r'^new_request/$', DatasetRequestView.as_view(), name='new_request'),
    url(r'^success/$', RequestSuccessView, name='request_success'),
)
