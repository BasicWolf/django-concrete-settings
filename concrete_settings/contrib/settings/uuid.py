import typing
from typing import Any, Tuple
from uuid import UUID

from concrete_settings import Validator, Undefined, registry
from concrete_settings.setting import Setting

if typing.TYPE_CHECKING:
    from concrete_settings.settings import Settings


class UUIDSetting(Setting):
    def __init__(
        self,
        value: Any = Undefined,
        *,
        doc: str = "",
        validators: Tuple[Validator, ...] = (),
        override: bool = False,
        **ignore
    ):
        super().__init__(
            value,
            doc=doc,
            validators=validators,
            type_hint=UUID,
            override=override,
        )

    def set_value(self, owner: "Settings", val):
        try:
            val = UUID(val)
        except ValueError:
            pass

        super().set_value(owner, val)


registry.register_setting(UUID, UUIDSetting)
