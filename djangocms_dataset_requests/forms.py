from django.forms import ModelForm, CharField, HiddenInput
from .models import DatasetRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset
from crispy_forms.bootstrap import FormActions, StrictButton

class RequestForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'request-form'
        self.helper.add_input(Submit('submit', 'Submit Request'))
        self.helper.form_action = 'new_request'
        self.helper.layout = Layout(
            Fieldset(
               'New Data Request',
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
