import unittest
from pathlib import Path

from python.main import validate_readme


class Tests(unittest.TestCase):
    def test_validate_readme(self: "Tests") -> None:
        with Path("prm/README").open(encoding="utf-8") as file:
            validate_readme(file)


if __name__ == "__main__":
    unittest.main()
