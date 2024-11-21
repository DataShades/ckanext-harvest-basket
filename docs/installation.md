# Installation

## Requirements

Compatibility with core CKAN versions:

| CKAN version | Compatible? |
|--------------|-------------|
| 2.9          | yes         |
| 2.10         | yes         |
| 2.11         | yes         |
| master       | not tested  |

## Installation

1. Install the extension from `PyPI`:
    ```sh
    pip install ckanext-harvest-basket
    ```

2. Enable the main plugin and harvesters you want to use in your CKAN configuration file (e.g. `ckan.ini` or `production.ini`):

    ```ini
    ckan.plugins = ... harvest_basket arcgis_harvester socrata_harvester ...
    ```

## Dependencies

The extension requires the following CKAN extensions to be installed and enabled:

1. [ckanext-harvest](https://github.com/ckan/ckanext-harvest):
This extension is built on top of ckanext-harvest. You need to install and enable it because ckanext-harvest-basket only provides the harvesters, not the harvesting process itself. Without it, the extension won’t work.

2. [ckanext-transmute](https://github.com/DataShades/ckanext-transmute) (_optional_):
If you want to modify remote data based on a schema in your harvest source configuration, you'll need to install and enable ckanext-transmute.

3. [ckanext-dcat](https://github.com/ckan/ckanext-dcat) (_optional_):
If you want to harvest metadata from DCAT JSON files, you'll need to install and enable ckanext-dcat, as we're inheriting the original DCAT harvester from there.

4. [ckanext-spatial](https://github.com/ckan/ckanext-spatial) (_optional_):
If you want to harvest metadata from CSW servers, you'll need to install and enable ckanext-spatial, as we're inheriting the original CSW harvester from there.
