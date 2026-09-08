"""PySTAC support for the MAAP DPS Metadata and Provenance Extension."""

from __future__ import annotations

from typing import Literal

from pystac.extensions.base import ExtensionManagementMixin, PropertiesExtension
from pystac.extensions.hooks import ExtensionHooks

from pystac import ExtensionTypeError, Item, STACObjectType

SCHEMA_URI = "https://maap-project.github.io/maap-dps-stac-extension/v0.1.0/schema.json"
ALGORITHM_NAME_PROP = "maap-dps:algorithm_name"
ALGORITHM_VERSION_PROP = "maap-dps:algorithm_version"
USERNAME_PROP = "maap-dps:username"
TAG_PROP = "maap-dps:tag"


class MaapDpsExtension(PropertiesExtension, ExtensionManagementMixin[Item]):
    """Access MAAP DPS metadata and provenance properties on a STAC Item."""

    name: Literal["maap-dps"] = "maap-dps"

    def __init__(self, item: Item) -> None:
        self.item = item
        self.properties = item.properties

    def apply(
        self,
        algorithm_name: str,
        algorithm_version: str,
        username: str,
        tag: str | None,
    ) -> None:
        """Set the required MAAP DPS metadata properties."""
        self.algorithm_name = algorithm_name
        self.algorithm_version = algorithm_version
        self.username = username
        self.tag = tag

    @property
    def algorithm_name(self) -> str | None:
        """Return the name of the algorithm that produced this Item."""
        return self._get_property(ALGORITHM_NAME_PROP, str)

    @algorithm_name.setter
    def algorithm_name(self, value: str | None) -> None:
        self._set_property(ALGORITHM_NAME_PROP, value)

    @property
    def algorithm_version(self) -> str | None:
        """Return the version of the algorithm that produced this Item."""
        return self._get_property(ALGORITHM_VERSION_PROP, str)

    @algorithm_version.setter
    def algorithm_version(self, value: str | None) -> None:
        self._set_property(ALGORITHM_VERSION_PROP, value)

    @property
    def username(self) -> str | None:
        """Return the username associated with the DPS submission."""
        return self._get_property(USERNAME_PROP, str)

    @username.setter
    def username(self, value: str | None) -> None:
        self._set_property(USERNAME_PROP, value)

    @property
    def tag(self) -> str | None:
        """Return the tag associated with the DPS submission."""
        return self._get_property(TAG_PROP, str)

    @tag.setter
    def tag(self, value: str | None) -> None:
        self._set_property(TAG_PROP, value, pop_if_none=False)

    @classmethod
    def get_schema_uri(cls) -> str:
        """Return the schema URI for this extension."""
        return SCHEMA_URI

    @classmethod
    def ext(cls, obj: Item, add_if_missing: bool = False) -> MaapDpsExtension:
        """Return the MAAP DPS extension wrapper for an Item."""
        if not isinstance(obj, Item):
            raise ExtensionTypeError(cls._ext_error_message(obj))
        cls.ensure_has_extension(obj, add_if_missing)
        return cls(obj)


class MaapDpsExtensionHooks(ExtensionHooks):
    """Register the MAAP DPS schema URI with PySTAC."""

    schema_uri = SCHEMA_URI
    prev_extension_ids: set[str] = set()
    stac_object_types = {STACObjectType.ITEM}


MAAP_DPS_EXTENSION_HOOKS: ExtensionHooks = MaapDpsExtensionHooks()
