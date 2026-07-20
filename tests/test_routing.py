from __future__ import annotations

import unittest

from validation.validate_routing import validate_routing


class RoutingTests(unittest.TestCase):
    def test_all_routed_skills_exist(self) -> None:
        self.assertEqual(validate_routing(), [])


if __name__ == "__main__":
    unittest.main()
