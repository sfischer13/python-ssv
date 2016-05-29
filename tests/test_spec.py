#!/usr/bin/env python

"""
test_spec
---------

Tests for the the SSV specification.
"""


import tempfile
import unittest

import ssv
from ssv.constant import RS
from ssv.constant import US


class TestSpec(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def check_in_out(self, table, string):
        string = string.replace("R", RS)
        string = string.replace("U", US)
        self.assertEqual(ssv.dumps(table), string)
        self.assertEqual(table, ssv.loads(string))

    def test_spec_000(self):
        self.check_in_out([[""]], "")

    def test_spec_001(self):
        self.check_in_out([[""], [""]], "R")

    def test_spec_002(self):
        self.check_in_out([["1"], [""]], "1R")

    def test_spec_003(self):
        self.check_in_out([[""], ["1"]], "R1")

    def test_spec_004(self):
        self.check_in_out([["1"], ["2"]], "1R2")

    def test_spec_005(self):
        self.check_in_out([[""], ["", ""]], "RU")

    def test_spec_006(self):
        self.check_in_out([[""], ["1", ""]], "R1U")

    def test_spec_007(self):
        self.check_in_out([[""], ["", "1"]], "RU1")

    def test_spec_008(self):
        self.check_in_out([[""], ["1", "2"]], "R1U2")

    def test_spec_009(self):
        self.check_in_out([["1"], ["2", "3"]], "1R2U3")


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
