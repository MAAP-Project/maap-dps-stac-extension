# MAAP DPS Metadata and Provenance Extension

- **Title:** MAAP DPS Metadata and Provenance Extension
- **Identifier:** <https://maap-project.github.io/maap-dps-stac-extension/v0.1.0/schema.json>
- **Field Name Prefix:** `maap-dps`
- **Scope:** Item Properties
- **Extension [Maturity Classification](https://github.com/radiantearth/stac-spec/tree/master/extensions/README.md#extension-maturity):** Proposal
- **Owner:** [MAAP-Project](https://github.com/MAAP-Project)

This extension defines metadata and provenance from the MAAP Data Processing
Service (DPS). Version 0.1.0 applies these fields to generated STAC Items. It
uses flat, namespaced Item Properties so the fields can be filtered through a
STAC API.

- [Item example](examples/item.json)
- [Published GitHub Pages site](https://maap-project.github.io/maap-dps-stac-extension/)
- [JSON Schema](json-schema/schema.json)
- [Changelog](CHANGELOG.md)

## Fields

These fields are available in STAC Item `properties` objects:

| Field Name | Type | Required | Description |
| --- | --- | --- | --- |
| `maap-dps:algorithm_name` | string | Yes | Name of the algorithm that produced the Item. |
| `maap-dps:algorithm_version` | string | Yes | Version of the algorithm that produced the Item. |
| `maap-dps:username` | string | Yes | Username associated with the DPS submission. |
| `maap-dps:tag` | string or null | Yes | Tag associated with the DPS submission. |

When the extension is declared in `stac_extensions`, all four extension fields
are required. No optional extension fields are defined in version 0.1.0. A job
identifier is intentionally not included because this version does not have a
verified stable source field and meaning for one.

Properties from STAC core and other extensions remain valid alongside these
fields. Unknown `maap-dps:` fields are not part of this version and are rejected
by the schema.

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

Then run the Markdown and example validation checks with:

```bash
npm test
```
