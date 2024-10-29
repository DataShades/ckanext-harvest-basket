import json
import logging
from urllib.parse import urljoin

import ckan.plugins.toolkit as tk
from ckan import model

from ckanext.harvest.harvesters import CKANHarvester
from ckanext.harvest.harvesters.ckanharvester import SearchError

from ckanext.harvest_basket.harvesters.base_harvester import BasketBasicHarvester


log = logging.getLogger(__name__)


class CustomCKANHarvester(CKANHarvester, BasketBasicHarvester):
    SRC_ID = "CKAN"

    def import_stage(self, harvest_object):
        package_dict = json.loads(harvest_object.content)
        self._set_config(harvest_object.source.config)
        self.transmute_data(package_dict, self.config.get("tsm_schema"))
        self.handle_conditions(
            package_dict,
            self.config.get("conditions", []),
            harvest_object.harvest_source_id)
        harvest_object.content = json.dumps(package_dict)

        super().import_stage(harvest_object)

    def _search_for_datasets(self, remote_ckan_base_url, fq_terms=None):
        pkg_dicts = super()._search_for_datasets(remote_ckan_base_url, fq_terms)
        max_datasets = int(self.config.get("max_datasets", 0))
        return pkg_dicts[:max_datasets] if max_datasets else pkg_dicts

    def _search_datasets(self, remote_url: str):
        url = remote_url.rstrip("/") + "/api/action/package_search?rows=1"
        resp = self._make_request(url)

        if not resp:
            return

        try:
            package_dict = json.loads(resp.text)["result"]["results"]
        except (ValueError, KeyError) as e:
            err_msg: str = f"{self.SRC_ID}: response JSON doesn't contain result: {e}"
            log.error(err_msg)
            raise SearchError(err_msg)

        return package_dict

    def fetch_stage(self, harvest_object):
        data_dict = json.loads(harvest_object.content)
        data_dict["type"] = "dataset"
        harvest_object.content = json.dumps(data_dict)
        return super().fetch_stage(harvest_object)

    def _pre_map_stage(self, data_dict, source_url):
        data_dict["type initial"] = data_dict["type"]
        data_dict["type"] = "dataset"
        return data_dict

    def transmute_data(self, data, schema):
        if schema:
            tk.get_action("tsm_transmute")(
                {
                    "model": model,
                    "session": model.Session,
                    "user": self._get_user_name(),
                },
                {"data": data, "schema": schema},
            )

    def handle_conditions(self, data, conditions, source_id):
        '''
            Specify conditions for fields, can be multiple conditions
            "conditions": [
                {"field": "FIELD_NAME",
                "source": "harvester_config", If the field should be taken from Harvester Dataset
                            Otherwise try to take the value from the Data Dict
                "case": "FIELD_VALUE_EQUAL",
                "then": "FIELD_TO_MODIFY",
                "value": "FIELD_TO_MODIFY_VALUE",
                "otherwise": "FIELD_TO_DEFAULT" Default value if check not passed. Optional
                },
                EXAMPLE
                {"field": "owner_org",
                "source": "harvester_config",
                "case": "77f83b6a-8541-4ae8-b439-011ed75b1564",
                "then": "groups",
                "value": [{"name":"society"}],
                "otherwise": [{"id":"transport"}]
                }
            ]
        '''
        source_dataset = tk.get_action('package_show')(
            {
                "model": model,
                "session": model.Session,
                "user": self._get_user_name(),
            }, {'id': source_id}
        )

        for condition in conditions:
            try:
                field = condition['field']
                source = condition.get('source')
                case = condition['case']
                then = condition['then']
                value = condition['value']
                otherwise = condition.get('otherwise')

                if source and source == 'harvester_config':
                    val = source_dataset[field]
                else:
                    val = data[field]

                if otherwise:
                    data[then] = value if val == case else otherwise
                elif val and val == case:
                    data[then] = value
            except KeyError as e:
                err_msg: str = f"Missing key: {e}"
                log.error(err_msg)
                raise AttributeError(*e.args)
