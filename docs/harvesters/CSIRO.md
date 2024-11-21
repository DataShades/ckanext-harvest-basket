The CSIRO harvester is a CKAN harvester that can be used to harvest metadata from [CSIRO data sources](https://data.csiro.au/).

CSIRO is Australia's national science research agency. It is a government agency that conducts scientific research to solve problems that are important to Australia and the world.

The CSIRO Data Access Portal provides access to research data, software and other digital assets published by CSIRO across a range of disciplines.

## Enable the Harvester

To enable the harvester, add `basket_csiro_harvester` to the `ckan.plugins` setting in your CKAN configuration file (e.g., `ckan.ini` or `production.ini`).

```ini
ckan.plugins = ... basket_csiro_harvester ...
```

## Configuration options

=== "Transmute Schema"
    {% include-markdown "./snippets/config_transmute_schema.md" %}
