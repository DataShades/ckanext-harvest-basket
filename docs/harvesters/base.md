We utilize different technologies to gather data from various platforms like ODS, ArcGIS, Socrata, DKAN, Junar, and more. With these harvesters, you can automatically pull datasets from different sources into your CKAN instance, helping you manage and share data more efficiently.

Some data portal provides an API to access their data, and some do not. For those that do not provide an API, we can use web scraping to gather data. Web scraping is a technique to extract data from websites. Web scraping is not so reliable, as using an API, but it is the only option when the data portal does not provide a public API.

Each harvester has an integration with the [ckanext-transmute](https://github.com/DataShades/ckanext-transmute) extension, which allows you to transform datasets during the harvesting process using a harvest source configuration.

It's helpful, when you need to adjust the result data to fit your CKAN instance dataset schema. To use the `ckanext-transmute`, you'll have to install and enable it in your CKAN instance. Other from that, you need to provide a `tsm_config` key into your harvest source configuration.

The syntax and all the information about installing and using the `ckanext-transmute` extension can be found in the [ckanext-transmute documentation](https://github.com/DataShades/ckanext-transmute)
