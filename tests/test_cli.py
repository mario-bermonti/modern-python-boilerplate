"""Tests for `modern_python_boilerplate`.cli module."""
from typing import List

import pytest
from click.testing import CliRunner

import modern_python_boilerplate
from modern_python_boilerplate import cli


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], "modern_python_boilerplate"),
        (["--help"], "Usage: main [OPTIONS]"),
        (["--version"], f"main, version { modern_python_boilerplate.__version__ }\n"),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, options)
    assert result.exit_code == 0
    assert expected in result.output
