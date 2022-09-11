import os
import unittest

from alan_rickman.gh import fetch

HERE = os.path.split(os.path.abspath(__file__))[0]


class TestFetch(unittest.TestCase):
    def test_fetch(self):
        url = fetch()
        self.assertGreater(len(url), 0)
