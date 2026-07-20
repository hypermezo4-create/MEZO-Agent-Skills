from __future__ import annotations

import unittest

from validation.validate_structure import validate_structure


class StructureTests(unittest.TestCase):
    def test_repository_structure_is_valid(self) -> None:
        self.assertEqual(validate_structure(), [])


if __name__ == "__main__":
    unittest.main()
