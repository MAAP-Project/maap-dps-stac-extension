# MAAP DPS Metadata and Provenance Extension

- **Title:** MAAP DPS Metadata and Provenance Extension
- **Identifier:** <https://maap-project.github.io/maap-dps-stac-extension/v0.1.0/schema.json>
- **Field Name Prefix:** `maap-dps`
- **Scope:** Item
- **Extension [Maturity Classification](https://github.com/radiantearth/stac-spec/tree/master/extensions/README.md#extension-maturity):** Proposal
- **Owner:** @hrodmn

This extension defines metadata and provenance from the MAAP Data Processing
Service (DPS). Version 0.1.0 applies these fields to generated STAC Items. It
uses flat, namespaced Item Properties so the fields can be filtered through a
STAC API.

- [Item example](examples/item.json)
- [JSON Schema](json-schema/schema.json)
- [Changelog](CHANGELOG.md)

## Fields

These fields are available in STAC Item `properties` objects:

| Field Name | Type | Required | Description |
| --- | --- | --- | --- |
| `maap-dps:algorithm_name` | string | Yes | Name of the algorithm that produced the Item. |
| `maap-dps:username` | string | Yes | Username associated with the DPS submission. |
| `maap-dps:tag` | string or null | Yes | Tag associated with the DPS submission. |

When the extension is declared in `stac_extensions`, all three extension fields
are required. No optional extension fields are defined in version 0.1.0.

### Algorithm version

Items must include `processing:version` from the
[Processing extension](https://github.com/stac-extensions/processing/tree/v1.2.0)
to record the version of the algorithm that produced the Item. This field is
required in addition to the three MAAP DPS fields above. Its definition and
validation belong to the Processing extension.

Items must also declare
`https://stac-extensions.github.io/processing/v1.2.0/schema.json` in
`stac_extensions`, as shown in the [Item example](examples/item.json).

## Versioning

Each released schema is published at:

`https://maap-project.github.io/maap-dps-stac-extension/v{version}/schema.json`

For example, the v0.1.0 schema is available at
<https://maap-project.github.io/maap-dps-stac-extension/v0.1.0/schema.json>.

## Contributing

All contributions are subject to the
[STAC Specification Code of Conduct](https://github.com/radiantearth/stac-spec/blob/master/CODE_OF_CONDUCT.md).

### Running tests

Install the Node.js dependencies once with:

```bash
npm install
```

Then run the schema tests, Markdown checks, and example validation with:

```bash
npm test
```
