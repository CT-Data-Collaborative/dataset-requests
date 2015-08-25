from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class DatasetRequestAndIssues(CMSApp):
    name = 'Dataset Request and Issue Tracking'
    urls = ['dataset-requests.urls']

apphook_pool.register(DatasetRequestAndIssues)
