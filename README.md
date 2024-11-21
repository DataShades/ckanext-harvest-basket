# Home

The **ckanext-harvest-basket** extension adds a set of custom harvesters to CKAN, making it easy to gather data from various platforms like ODS, ArcGIS, Socrata, DKAN, Junar, and more. With these harvesters, you can automatically pull datasets from different sources into your CKAN instance, helping you manage and share data more efficiently.

Key features:

* Harvesters for popular data platforms, including CKAN, ODS, ArcGIS, Socrata, DKAN, Junar and others.
* Integration with the [ckanext-transmute](https://github.com/DataShades/ckanext-transmute) extension, which allows you to transform datasets during the harvesting process using a harvest source configuration.
* Source checkup preview. When creating a source, the harvester will try to connect to the remote portal and harvest one dataset to check if it’s accessible.
* Anonymous user restrictions. You can disallow anonymous users from accessing harvester pages.

See the [documentation](https://datashades.github.io/ckanext-harvest-basket/) for more information.

## Quick start

1. Install the extension from `PyPI`:
    ```bash
    pip install ckanext-harvest-basket
    ```

2. Enable the main plugin and harvesters you want to use in your CKAN configuration file (e.g. `ckan.ini` or `production.ini`):

    ```ini
    ckan.plugins = ... harvest_basket arcgis_harvester socrata_harvester ...
    ```

## Developer installation

To install `ckanext-harvest-basket` for development, activate your CKAN virtualenv and
do:

```bash
git clone https://github.com/DataShades/ckanext-harvest-basket.git
cd ckanext-harvest-basket
pip install -e '.[dev]'
```


## Tests

To run the tests, do:

```bash
pytest --ckan-ini=test.ini
```

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
