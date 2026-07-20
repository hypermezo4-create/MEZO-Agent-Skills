from __future__ import annotations

import unittest

from validation.validate_links import validate_links


class LinkTests(unittest.TestCase):
    def test_internal_markdown_links_resolve(self) -> None:
        self.assertEqual(validate_links(), [])


if __name__ == "__main__":
    unittest.main()
