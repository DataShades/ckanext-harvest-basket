from __future__ import annotations

import json

from typing import Any, Optional

import ckan.plugins.toolkit as tk

from ckanext.harvest_basket.harvesters import DKANHarvester
from ckanext.harvest_basket.harvesters import JunarHarvester


@tk.side_effect_free
def check_source(ctx: dict[str, Any], data_dict: dict) -> dict[str, Any]:
    tk.check_access("harvest_basket_check_source", ctx, data_dict)

    source_name: str = tk.get_or_bust(data_dict, "source_name")
    source_url: Optional[str] = data_dict.get("source_url")
    config: dict = json.loads(data_dict.get("config", "{}"))
    
    if not source_url:
        raise tk.ValidationError(f"The source URL must be provided to make a checkup")

    sources = {
        "dkan": DKANHarvester,
        "junar": JunarHarvester
    }

    harvester_class = sources.get(source_name)
    
    if not harvester_class:
        raise tk.ValidationError(f"The source checkup for type `{source_name}` not implemented")
    
    return harvester_class().make_checkup(source_url, config)