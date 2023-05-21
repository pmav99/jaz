from __future__ import annotations

import os
from typing import Any
from typing import Callable

try:
    from ansible.plugins.test.core import TestModule
    from ansible.plugins.filter.core import FilterModule

    _ANSIBLE_IS_AVAILABLE = True
except ImportError:
    _ANSIBLE_IS_AVAILABLE = False


def from_env(value: str, default: str = "") -> str:
    return os.environ.get(value, default)


FILTERS: dict[str, Callable[[Any], Any]] = {
    "env": from_env,
}


if _ANSIBLE_IS_AVAILABLE:
    FILTERS.update(FilterModule().filters())
    FILTERS.update(TestModule().tests())
