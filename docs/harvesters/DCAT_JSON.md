The DCAT JSON harvester is a CKAN harvester that can be used to harvest metadata from [DCAT JSON files](https://www.w3.org/TR/vocab-dcat-2/).

DCAT is an RDF vocabulary designed to facilitate interoperability between data catalogs published on the Web. 

!!! warning
    This harvester is based on the original DCAT harvester from [ckanext-dcat](https://github.com/ckan/ckanext-dcat),
    therefore it requires the `ckanext-dcat` library to be installed.

## Enable the Harvester

To enable the harvester, add `basket_dcat_json_harvester` to the `ckan.plugins` setting in your CKAN configuration file (e.g., `ckan.ini` or `production.ini`).

```ini
ckan.plugins = ... basket_dcat_json_harvester ...
```

## Configuration options


=== "Transmute Schema"
    {% include-markdown "./snippets/config_transmute_schema.md" %}
