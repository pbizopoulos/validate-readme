import unittest
from pathlib import Path

from python.main import readme_validator


class Tests(unittest.TestCase):
    def test_readme_validator(self: "Tests") -> None:
        with Path("prm/README").open(encoding="utf-8") as file:
            readme_validator(file)


if __name__ == "__main__":
    unittest.main()
