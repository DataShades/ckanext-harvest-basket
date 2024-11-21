# OpenDataSoft

The OpenDataSoft Harvester is a CKAN harvester that allows to harvest datasets from [OpenDataSoft](https://www.opendatasoft.com/en/) platforms.

OpenDataSoft is a cloud-based turnkey platform for data publishing and API management. It is designed for data owners who need to share data with a larger audience in a simple and cost-effective way.

## Enable the Harvester

To enable the harvester, add `ods_harvester` to the `ckan.plugins` setting in your CKAN configuration file (e.g., `ckan.ini` or `production.ini`).

```ini
ckan.plugins = ... ods_harvester ...
```

## Configuration options

=== "Where"
    {% include-markdown "./snippets/config_where.md" %}

=== "Max Datasets"
    {% include-markdown "./snippets/config_max_datasets.md" %}

=== "Transmute Schema"
    {% include-markdown "./snippets/config_transmute_schema.md" %}
