const assert = require('node:assert/strict');
const { test } = require('node:test');
const Ajv = require('ajv');
const schema = require('../json-schema/schema.json');
const example = require('../examples/item.json');

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
