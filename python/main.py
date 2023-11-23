from __future__ import annotations

import unittest
from io import TextIOWrapper
from pathlib import Path

from lark import Lark

grammar = """
start: title requirements? download? development? staging? production? installation? usage?
title: "# " LINE+ "\\n"
requirements: "# Requirements" "\\n" LINE+ "\\n"
download: "# Download\\n" LINE+ "\\n"
development: "# Development\\n" LINE+ "\\n"
staging: "# Staging\\n" LINE+ "\\n"
production: "# Production\\n" LINE+ "\\n"
installation: "# Installation\\n" LINE+ "\\n"
usage: "# Usage\\n" LINE+ "\\n"
LINE: /.+[^\\s]\\n/
"""  # noqa: E501


def validate_readme(code_input: str | TextIOWrapper) -> None:
    parser = Lark(grammar, parser="lalr")
    if isinstance(code_input, str):
        with Path(code_input).open() as file:
            parser.parse(file.read())
    elif isinstance(code_input, TextIOWrapper):
        parser.parse(code_input.read())


class Tests(unittest.TestCase):
    def test_validate_readme(self: Tests) -> None:
        with Path("prm/README").open(encoding="utf-8") as file:
            validate_readme(file)


def main() -> None:
    import fire

    fire.Fire(validate_readme)


if __name__ == "__main__":
    unittest.main()
