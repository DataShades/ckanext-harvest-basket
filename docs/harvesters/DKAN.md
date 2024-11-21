The DKAN harvester is a CKAN harvester that can be used to harvest metadata from [DKAN open data portals](https://dkan.readthedocs.io/en/latest/).

DKAN is a Drupal-based community-driven, free and open source open data platform that gives organisations and individuals ultimate freedom to publish and consume structured information.

## Enable the Harvester

To enable the harvester, add `dkan_harvester` to the `ckan.plugins` setting in your CKAN configuration file (e.g., `ckan.ini` or `production.ini`).

```ini
ckan.plugins = ... dkan_harvester ...
```

## Configuration options

=== "Delay"
    {% include-markdown "./snippets/config_delay.md" %}

=== "Max Datasets"
    {% include-markdown "./snippets/config_max_datasets.md" %}

=== "Transmute Schema"
    {% include-markdown "./snippets/config_transmute_schema.md" %}
