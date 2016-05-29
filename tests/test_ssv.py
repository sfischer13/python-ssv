#!/usr/bin/env python

"""
test_ssv
--------

Tests for the `ssv` module.
"""


import tempfile
import unittest

import ssv


TABLE = [['1', 'Alfa', 'V'],
         ['2', 'Bravo', 'C'],
         ['3', 'Charlie', 'C'],
         ['4', 'Delta', 'C'],
         ['5', 'Echo', 'V'],
         ['6', 'Foxtrot', 'C'],
         ['7', 'Golf', 'C'],
         ['8', 'Hotel', 'C'],
         ['9', 'India', 'V'],
         ['10', 'Juliett', 'C']]


class TestSSV(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_dump_load(self):
        with tempfile.TemporaryFile('w+t') as tmp:
            ssv.dump(TABLE, tmp)
            tmp.seek(0)
            table = ssv.load(tmp)
            self.assertEqual(table, TABLE)

    def test_001_dumpf_loadf(self):
        with tempfile.NamedTemporaryFile('w+t') as tmp:
            path = tmp.name
            ssv.dumpf(TABLE, path)
            table = ssv.loadf(path)
            self.assertEqual(table, TABLE)

    def test_002_dumps_loads(self):
        string = ssv.dumps(TABLE)
        table = ssv.loads(string)
        self.assertEqual(table, TABLE)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
