The CKAN harvester can be used to harvest metadata from other CKAN Data Portals.

We altered the original CKAN harvester to allow using the Transmute schema to make a harvester more flexible.

## Enable the Harvester

To enable the harvester, add `custom_ckan_harvester` to the `ckan.plugins` setting in your CKAN configuration file (e.g., `ckan.ini` or `production.ini`).

```ini
ckan.plugins = ... custom_ckan_harvester ...
```

## Configuration options

=== "Default CKAN Harvester Configuration"
    Since we're just inheriting the original CKAN harvester, you still can use the original configuration options. Check the original `ckanext-harvest` [documentation](https://github.com/ckan/ckanext-harvest?tab=readme-ov-file#the-ckan-harvester) for more information.

=== "Max Datasets"
    {% include-markdown "./snippets/config_max_datasets.md" %}

=== "Transmute Schema"
    {% include-markdown "./snippets/config_transmute_schema.md" %}
