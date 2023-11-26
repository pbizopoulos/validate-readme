from __future__ import annotations

import unittest
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


def validate_readme(input_file_name: str | bytes) -> None:
    parser = Lark(grammar, parser="lalr")
    if isinstance(input_file_name, str):
        with Path(input_file_name).open() as file:
            parser.parse(file.read())
    else:
        parser.parse(input_file_name.decode())


class Tests(unittest.TestCase):
    def test_validate_readme_bytes_input(self: Tests) -> None:
        with Path("prm/README").open(encoding="utf-8") as file:
            bytes_input = file.read().encode("utf-8")
            validate_readme(bytes_input)

    def test_validate_readme_file_input(self: Tests) -> None:
        validate_readme("prm/README")


def main() -> None:
    import fire

    fire.Fire(validate_readme)


if __name__ == "__main__":
    unittest.main()
