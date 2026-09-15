"""Checks for the MAAP DPS PySTAC extension."""

from datetime import datetime, timezone

import pystac
from pystac.extensions.maap_dps import (
    PROCESSING_SCHEMA_URI,
    SCHEMA_URI,
    MaapDpsExtension,
)


def test_apply_and_discover_extension() -> None:
    """Apply the extension and confirm its installed entry point is discovered."""
    item = pystac.Item("example", None, None, datetime.now(timezone.utc), {})
    MaapDpsExtension.ext(item, add_if_missing=True).apply(
        algorithm_name="example-algorithm",
        algorithm_version="1.0.0",
        username="example-user",
        tag=None,
    )

    properties = item.to_dict()["properties"]
    assert properties["maap-dps:algorithm_name"] == "example-algorithm"
    assert properties["processing:version"] == "1.0.0"
    assert properties["maap-dps:username"] == "example-user"
    assert properties["maap-dps:tag"] is None
    assert item.stac_extensions == [SCHEMA_URI, PROCESSING_SCHEMA_URI]

    pystac.EXTENSION_HOOKS.get_deprecation_message(item)
    assert SCHEMA_URI in pystac.EXTENSION_HOOKS.hooks
