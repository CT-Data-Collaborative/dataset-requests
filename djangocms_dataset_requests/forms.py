from django.forms import ModelForm, CharField, HiddenInput
from .models import DatasetRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import FormActions, StrictButton

class RequestForm(ModelForm):
    # plugin_id = CharField(widget=HiddenInput)
    # redirect_url = CharField(widget=HiddenInput)

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'request-form'
        self.helper.add_input(Submit('submit', 'Submit Request'))
        self.helper.form_action = 'new_request'
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
