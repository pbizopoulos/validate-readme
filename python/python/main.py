from __future__ import annotations

import sys
from io import TextIOWrapper
from pathlib import Path

from lark import Lark

if __name__ == "__main__":
    readme_file = "prm/readme.peg"
else:
    readme_file = "python/prm/readme.peg"

def readme_validator(code_input: str | TextIOWrapper) -> None:
    with Path(readme_file).open() as file:
        parser = Lark(file.read(), parser="lalr")
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
