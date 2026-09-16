"""Checks for the MAAP DPS PySTAC extension."""

from datetime import datetime, timezone

import pytest

import pystac
from pystac import RequiredPropertyMissing
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
        processing_version="1.0.0",
        username="example-user",
        tag=None,
    )

    extension = MaapDpsExtension.ext(item)
    assert extension.algorithm_name == "example-algorithm"
    assert extension.processing_version == "1.0.0"
    assert extension.username == "example-user"
    assert extension.tag is None

    properties = item.to_dict()["properties"]
    assert properties["maap-dps:algorithm_name"] == "example-algorithm"
    assert properties["processing:version"] == "1.0.0"
    assert properties["maap-dps:username"] == "example-user"
    assert properties["maap-dps:tag"] is None
    assert item.stac_extensions == [SCHEMA_URI, PROCESSING_SCHEMA_URI]

    pystac.EXTENSION_HOOKS.get_deprecation_message(item)
    assert SCHEMA_URI in pystac.EXTENSION_HOOKS.hooks


@pytest.mark.parametrize("name", ["algorithm_name", "processing_version", "username"])
@pytest.mark.parametrize(
    "properties",
    [
        {},
        {
            "maap-dps:algorithm_name": None,
            "processing:version": None,
            "maap-dps:username": None,
        },
    ],
)
def test_required_properties(name: str, properties: dict[str, None]) -> None:
    """Required getters reject missing or null values while tag stays nullable."""
    item = pystac.Item("example", None, None, datetime.now(timezone.utc), properties)
    extension = MaapDpsExtension.ext(item, add_if_missing=True)
    with pytest.raises(RequiredPropertyMissing):
        getattr(extension, name)
    assert extension.tag is None
