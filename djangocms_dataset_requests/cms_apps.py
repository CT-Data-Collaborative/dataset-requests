from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class DatasetRequests(CMSApp):
    name = _('Dataset Requests')
    urls = ['djangocms_dataset_requests.urls']

apphook_pool.register(DatasetRequests)
