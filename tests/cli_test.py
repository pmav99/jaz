from __future__ import annotations

from jaz._cli import app


def test_app_help(runner):
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "jaz" in result.stdout
    assert "--help" in result.stdout


def test_app_version(runner):
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert len(result.stdout.splitlines()) == 1
    assert "jaz" in result.stdout
    version = result.stdout.split(" ")[-1]
    for part in version.split(".")[:3]:
        assert part.isdigit()
