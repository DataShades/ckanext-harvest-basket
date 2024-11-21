**`tsm_schema`** [_optional_]

Transmute schema allows you to define a schema that will be used to transform the
harvested data before we're trying to create/update a dataset in CKAN.

This is useful when the harvested data doesn't match the CKAN dataset schema and
you need to transform it.

Otherwise, you'd need to write a custom harvester and process the remote data yourself.

See the `ckanext-transmute` [documentation](https://github.com/DataShades/ckanext-transmute?tab=readme-ov-file#working-with-transmute) to learn more about the transmute schema syntax.

{% include-markdown "./tsm_example.md" %}

**Type**: `dict[str, Any]`

**Default**: `None`
