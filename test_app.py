import unittest

import app


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(40, 2), 42)
