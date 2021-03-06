from typing import TYPE_CHECKING, Optional

from typing_extensions import Protocol


if TYPE_CHECKING:
    from ..settings import Settings
    from .. import Setting


class Validator(Protocol):
    """A validator is a callable that raises an exception if a value is wrong.

    A validator accepts a value as a mandatory argument, and keyword-only arguments
    referring to settings, setting and setting's name."""

    def __call__(
        self,
        value,
        *,
        name: Optional[str] = None,
        owner: Optional['Settings'] = None,
        setting: Optional['Setting'] = None,
    ):
        """Validate a value. Raise `ValidationError` if value is wrong."""
        ...
