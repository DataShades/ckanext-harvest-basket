# Troubleshooting

This page contains some common issues and solutions when using the Harvest Basket.

## Missing **"Source checkup preview"** form field during harvest source creation.

This happens, because of the way how CKAN loads the extension templates. The harvest basket extension templates are being replaced with the original `ckanext-harvester` templates.

To fix it, place the `harvest_basket` extension before the `harvest` extension in the `ckan.plugins` configuration in your CKAN configuration file.

```ini
ckan.plugins = harvest_basket harvest
```

