from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import DatasetRequest, Source

class SourceAdmin(admin.ModelAdmin):
    pass

class DatasetRequestAdmin(admin.ModelAdmin):
    list_display = ('dataset_name', 'dataset_description', 'dataset_source', 'status')
    search_fields = ('status', 'dataset_source', 'datset_description', 'dataset_name')
    list_filter = ('status', 'dataset_source', 'user_notified')
    readonly_fields = ('created_date',)

    _fieldsets = (
        (_('Request Detail'), {
            'fields': (
                'created_date', 'dataset_name', 'dataset_source',  'dataset_description', 'status', 'response', 'trello_id'
                )
            }
        ),
        (_('User Info'), {
            'fields': (
                'user_first_name', 'user_last_name', 'user_email', 'user_notified',
                )
            }
        )
    )

    def get_fieldsets(self, request, obj=None):
        return self._fieldsets

admin.site.register(Source, SourceAdmin)
admin.site.register(DatasetRequest, DatasetRequestAdmin)
