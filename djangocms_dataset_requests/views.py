from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.generic import FormView, DetailView

from .forms import RequestForm
from .models import DatasetRequest, Source, DatasetRequestPlugin

from trello import TrelloClient

class DatasetRequestView(FormView):
    """Capture request and trigger call to Trello API as defined in plugin"""
    form_class = RequestForm
    template_name = 'djangocms_dataset_requests/dataset_request.html'

    def update_trello(self, cleaned_data):
        plugin = get_object_or_404(DatasetRequestPlugin,
            pk=cleaned_data['plugin_id'])

        c = TrelloClient(plugin.api_key, plugin.trello_token)
        b = c.get_board(plugin.trello.board)
        # Currently we default to adding card to first list
        l = b.all_lists[0]
        label_list = b.get_labels()
        ds_name = "%s - %s" % (cleaned_data.dataset_name, dataset_source)
        ds_description = "%s\n%s\nRequested by: %s %s, %s on %s" % \
            (cleaned_data.dataset_name,
            cleaned_data.dataset_description,
            cleaned_data.user_first_name,
            cleaned_data.user_last_name,
            cleaned_data.user_email,
            cleaned_data.created_date)

        try:
            label_to_add = next(x for x in label_list if x.name == plugin.label_name)
        except StopIteration:
            label_to_add = b.add_label(plugin.label_name, "lime")

        try:
            card = l.add_card(ds_name, ds_description, label_to_add)
        except Exception:
            return Exception


    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        form.save(commit=True)
        success_url = '/'

        try:
            self.update_trello(cleaned_data)
        except:
            pass

        messages.success(self.request,'Your dataset request has been recorded. Thanks!')
        # return super(DatasetRequestView, self).form_valid(form)
        return redirect('/')
        #return redirect(cleaned_data['redirect_url'])

    # def form_invalid(self, form):
    #     redirect_url = form.data.get('redirect_url')

    #     if redirect_url:
    #         message = _(u'Something is wrong with your request.')
    #         messages.error(self.request, message)
    #         response = HttpResponseRedirect(redirect_url)
    #     else:
    #         # user has tampered with the redirect_url field.
    #         response = HttpResponseBadRequest()
    #     return response


class RequestDetail(DetailView):
    model = DatasetRequest

    @property
    def template_name_suffice(self):
        return '_detail'

    def get_queryset(self):
        return self.model.objects.all()

request_detail = RequestDetail.as_view()
