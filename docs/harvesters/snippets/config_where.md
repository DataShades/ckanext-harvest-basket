**`where`** [_optional_]

The `where` parameter is used to filter the results returned by the remote API.

A `where` filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) and lots of other functions to perform complex and precise search operations.

For more information, see [Opendatasoft Query Language](https://help.opendatasoft.com/apis/ods-explore-v2/#section/Opendatasoft-Query-Language-(ODSQL)/Where-clause) (ODSQL) reference documentation.


!!! Example
    ```sh
    my_numeric_field > 10 and my_text_field like "paris" or within_distance(my_geo_field, geom'POINT(1 1)', 1km)
    ```

**Type**: `str`

**Default**: `None`
