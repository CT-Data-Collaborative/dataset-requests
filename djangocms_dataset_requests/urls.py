from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(,
    # URL pattern for the UserListView  # noqa
    url(r'^$', views.RequestsHomeView, name='request_home'),
    url(r'^new_request/$', views.DatasetRequestView.as_view(), name='new_request'),
    url(r'^success/$', views.RequestSuccessView, name='request_success'),
)
