The CSW harvester is a CKAN harvester that can be used to harvest metadata from CSW servers. Catalogue Service for the Web (CSW), sometimes seen as Catalogue Service - Web, is a standard for exposing a catalogue of geospatial records in XML on the Internet (over HTTP). The catalogue is made up of records that describe geospatial data (e.g. KML), geospatial services (e.g. WMS), and related resources. 

!!! warning

    The harvester relies on the [`OWSLib` library](https://owslib.readthedocs.io/en/latest/introduction.html) to interact with the CSW server. To install the required dependencies, install the `ckanext-harvest-basket` package with the `[csw]` extra:

    ```bash
    pip install 'ckanext-harvest-basket[csw]'
    ```
## Enable the Harvester

To enable the harvester, add `basket_csw_harvester` to the `ckan.plugins` setting in your CKAN configuration file (e.g., `ckan.ini` or `production.ini`).

```ini
ckan.plugins = ... basket_csw_harvester ...
```

## Configuration options


=== "Transmute Schema"
    {% include-markdown "./snippets/config_transmute_schema.md" %}
