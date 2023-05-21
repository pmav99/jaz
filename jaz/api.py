from __future__ import annotations

import os
import pathlib
import sys

import jinja2

from ._filters import FILTERS
from ._globals import GLOBALS


def render(*, path: pathlib.Path, no_env: bool, output: pathlib.Path | None) -> None:
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(path),
    )
    env.filters.update(FILTERS)
    env.globals.update(GLOBALS)
    if not no_env:
        env.globals.update(os.environ)

    contents = sys.stdin.read() if str(path) == "-" else path.read_text()
    template = env.from_string(contents)
    rendered = template.render()
    if output:
        output.write_text(rendered)
    else:
        sys.stdout.write(rendered)
