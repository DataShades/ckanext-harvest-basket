from __future__ import annotations

import json
import logging

from ckanext.dcat.harvesters import DCATJSONHarvester
from ckanext.transmute.utils import get_schema

from .base_harvester import BasketBasicHarvester

log = logging.getLogger(__name__)

class BasketDcatJsonHarvester(DCATJSONHarvester, BasketBasicHarvester):
    SRC_ID = "DCAT"

    def info(self):
        return {
            "name": "basket_dcat_json",
            "title": "Extended DCAT JSON Harvester",
            "description": "Harvester with extended configuration "
            + "for DCAT dataset descriptions serialized as JSON",
        }

    def modify_package_dict(self, package_dict, dcat_dict, harvest_object):
        self.base_context = {"user": self._get_user_name()}

        package_dict = json.loads(harvest_object.content)
        self._set_config(harvest_object.source.config)

        self._transmute_content(package_dict)
        return package_dict
    
    def import_stage(self, harvest_object):
        result = False
        try:
            result = super().import_stage(harvest_object)
        except Exception as e:
            log.error(f"{self.SRC_ID}: import stage failed: {e}")
            return result
