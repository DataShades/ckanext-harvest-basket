The Socrata harvester is a CKAN harvester that can be used to harvest metadata from [Socrata open data portals](https://dev.socrata.com/).

Socrata is a company that provides an open data repository service that many government agencies use to make open data available to the public.

## Enable the Harvester

To enable the harvester, add `socrata_harvester` to the `ckan.plugins` setting in your CKAN configuration file (e.g., `ckan.ini` or `production.ini`).

```ini
ckan.plugins = ... socrata_harvester ...
```

## Configuration options

=== "Limit"
    {% include-markdown "./snippets/config_limit.md" %}

=== "Max Datasets"
    {% include-markdown "./snippets/config_max_datasets.md" %}

=== "Transmute Schema"
    {% include-markdown "./snippets/config_transmute_schema.md" %}
