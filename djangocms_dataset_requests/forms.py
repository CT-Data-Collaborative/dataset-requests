from django.forms import ModelForm, CharField, HiddenInput
from .models import DatasetRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import FormActions, StrictButton

class RequestForm(ModelForm):
    # plugin_id = CharField(widget=HiddenInput)
    # redirect_url = CharField(widget=HiddenInput)

    def update_trello(self):
        # Create a new trello card using the self.cleaned_data dictionary
        print self
        # def update_trello(self, cleaned_data):
        #     api_key = settings.TRELLO_API
        #     token = settings.TRELLO_TOKEN
        #     board = settings.TRELLO_REQUEST_BOARD
        #
        #     c = TrelloClient(api_key, token)
        #     b = c.get_board(board)
        #     # Currently we default to adding card to first list
        #     l = b.all_lists[0]
        #     label_list = b.get_labels()
        #     ds_name = "%s - %s" % (cleaned_data.dataset_name, dataset_source)
        #     ds_description = "%s\n%s\nRequested by: %s %s, %s on %s" % \
        #         (cleaned_data.dataset_name,
        #         cleaned_data.dataset_description,
        #         cleaned_data.user_first_name,
        #         cleaned_data.user_last_name,
        #         cleaned_data.user_email,
        #         cleaned_data.created_date)
        #
        #     try:
        #         label_to_add = next(x for x in label_list if x.name == plugin.label_name)
        #     except StopIteration:
        #         label_to_add = b.add_label(plugin.label_name, "lime")
        #
        #     try:
        #         card = l.add_card(ds_name, ds_description, label_to_add)
        #     except Exception:
        #         return Exception

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'request-form'
        self.helper.add_input(Submit('submit', 'Submit Request'))
        self.helper.form_action = 'requests:new_request'
        # self.helper.label_class = 'col-lg-2'
        # self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset(
               'Dataset Details',
               'dataset_name',
               'dataset_source',
               'dataset_description',
            ),
            Fieldset(
               'User Details',
               'user_first_name',
               'user_last_name',
               'user_email'
            )
        )

    class Meta:
        model = DatasetRequest
        fields = ['dataset_name', 'dataset_source', 'dataset_description',
            'user_first_name', 'user_last_name', 'user_email']
