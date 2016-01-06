# from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
#from django.template import RequestContext
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic import FormView, DetailView, ListView

from .forms import RequestForm
from .models import DatasetRequest, Source


#from trello import TrelloClient

class DatasetRequestsListView(ListView):
    model = DatasetRequest
    context_object_name = 'dataset_requests'


class DatasetRequestDetailView(DetailView):
    model = DatasetRequest
    template_name = 'djangocms_dataset_requests/datasetrequest_detail.html'
    context_object_name = 'dsr'


class DatasetRequestView(FormView):
    """Capture request and save"""
    form_class = RequestForm
    template_name = 'djangocms_dataset_requests/dataset_request.html'
    model = DatasetRequest

    def form_valid(self, form):
        form.save()
        return redirect('dataset_requests')

    def form_invalid(self, form):
        redirect_url = '/'

        if redirect_url:
            message = _(u'Something is wrong with your request.')
            messages.error(self.request, message)
            response = HttpResponseRedirect(redirect_url)
        else:
            # user has tampered with the redirect_url field.
            response = HttpResponseBadRequest()
        return response
