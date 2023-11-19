from __future__ import annotations

import sys
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
"""


def readme_validator(code_input: str | TextIOWrapper) -> None:
    parser = Lark(grammar, parser="lalr")
    if isinstance(code_input, str):
        with Path(code_input).open() as file:
            parser.parse(file.read())
    elif isinstance(code_input, TextIOWrapper):
        parser.parse(code_input.read())


def main() -> None:
    num_arguments_allowed = 2
    if len(sys.argv) == num_arguments_allowed:
        readme_validator(sys.argv[1])


if __name__ == "__main__":
    main()
