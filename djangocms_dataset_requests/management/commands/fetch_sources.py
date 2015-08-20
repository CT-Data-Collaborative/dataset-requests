# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.text import slugify

import ckanapi
from ...models import Source

class Command(BaseCommand):

    def get_sources(self, ckan):
        orgs = ckan.action.organization_list(all_fields=True)
        return [x['display_name'] for x in orgs]

    def handle(self, *args, **options):
        ckanurl = settings.CKAN_SITE_URL
        ckansite = ckanapi.RemoteCKAN(ckanurl)
        sources = self.get_sources(ckan)
        sources.append("Other")

        for s in sources:
            try:
                Source.objects.get(source_name=s)
            except DoesNotExist:
                new_source = Source()
                new_source.source_name = s
                new_source.save()
        
