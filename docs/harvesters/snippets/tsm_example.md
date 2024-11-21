??? example
    ```json
    {
        "root": "Dataset",
        "types": {
            "Dataset": {
                "fields": {
                    "title": {
                        "validators": [
                            "tsm_string_only",
                            "tsm_to_lowercase",
                            "tsm_name_validator"
                        ],
                        "map": "name"
                    },
                    "resources": {
                        "type": "Resource",
                        "multiple": true,
                        "map": "attachments"
                    },
                    "metadata_created": {
                        "validators": [
                            "tsm_isodate"
                        ],
                        "default": "2022-02-03T15:54:26.359453"
                    },
                    "metadata_modified": {
                        "validators": [
                            "tsm_isodate"
                        ],
                        "default_from": "metadata_created"
                    },
                    "metadata_reviewed": {
                        "validators": [
                            "tsm_isodate"
                        ],
                        "replace_from": "metadata_modified"
                    },
                }
            },
            "Resource": {
                "fields": {
                    "title": {
                        "validators": [
                            "tsm_string_only"
                        ],
                        "map": "name"
                    },
                    "extension": {
                        "validators": [
                            "tsm_string_only",
                            "tsm_to_uppercase"
                        ],
                        "map": "format"
                    },
                    "web": {
                        "validators": [
                            "tsm_string_only"
                        ],
                        "map": "url"
                    },
                    "sub-resources": {
                        "type": "Sub-Resource",
                        "multiple": true
                    },
                },
            }
        }
    }
    ```
