const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { test } = require('node:test');
const Ajv = require('ajv');
const packageJson = require('../package.json');
const schema = require('../json-schema/schema.json');
const example = require('../examples/item.json');

const schemaUrl = `https://maap-project.github.io/maap-dps-stac-extension/v${packageJson.version}/schema.json`;

test('published references use the package version', () => {
  assert.equal(schema.$id, schemaUrl);
  assert.equal(schema.properties.stac_extensions.allOf[0].contains.const, schemaUrl);
  assert.ok(example.stac_extensions.includes(schemaUrl));

  for (const script of ['check-examples', 'format-examples']) {
    assert.ok(packageJson.scripts[script].includes(schemaUrl));
  }

  const readme = readFileSync('README.md', 'utf8');
  assert.ok(readme.includes(`Version ${packageJson.version} applies`));
  assert.ok(readme.includes(`version ${packageJson.version}.`));
  assert.equal(readme.split(schemaUrl).length - 1, 2);
});

test('DPS requires the processing version and extension declaration', () => {
  const validate = new Ajv({ strict: false }).compile(schema);
  assert.equal(validate(example), true);

  const missingVersion = structuredClone(example);
  delete missingVersion.properties['processing:version'];
  assert.equal(validate(missingVersion), false);

  const missingExtension = structuredClone(example);
  missingExtension.stac_extensions = [schema.$id];
  assert.equal(validate(missingExtension), false);

  const legacyVersion = structuredClone(example);
  legacyVersion.properties['maap-dps:algorithm_version'] = '1.0.0';
  assert.equal(validate(legacyVersion), false);
});
