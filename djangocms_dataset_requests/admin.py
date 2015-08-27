from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# from adminsortable.admin import SortableAdmin, SortableTabularInline

from .models import DatasetRequest, Source

# class SourceInline(SortableTabularInline):
#     model = Source
#     extra = 0
#
# class SourceAdmin(SortableAdmin):
#     inlines = (SourceInline,)

class SourceAdmin(admin.ModelAdmin):
    pass

class DatasetRequestAdmin(admin.ModelAdmin):
    list_display = ('dataset_name', 'dataset_description', 'dataset_source', 'status')
    search_fields = ('status', 'dataset_source', 'datset_description', 'dataset_name')
    list_filter = ('status', 'dataset_source', 'user_notified')
    # readonly_fields = ('created_date', 'user_first_name', 'user_last_name', 'user_email')

    _fieldsets = (
        (_('Request Detail'), {
            'fields': (
                'dataset_source', 'dataset_name', 'dataset_description', 'status', 'created_date', 'trello_id'
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
