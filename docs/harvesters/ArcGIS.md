The ArcGIS harvester is a CKAN harvester that can be used to harvest metadata from [ArcGIS open data portals](https://www.arcgis.com/).

ArcGIS is a platform for organizations to create, manage, share, and analyze spatial data.

## Enable the Harvester

To enable the harvester, add `arcgis_harvester` to the `ckan.plugins` setting in your CKAN configuration file (e.g., `ckan.ini` or `production.ini`).

```ini
ckan.plugins = ... arcgis_harvester ...
```


## Configuration options

=== "Max Datasets"
    {% include-markdown "./snippets/config_max_datasets.md" %}

=== "Transmute Schema"
    {% include-markdown "./snippets/config_transmute_schema.md" %}
