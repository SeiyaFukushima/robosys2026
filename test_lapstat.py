#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Seiya Fukushima
# SPDX-License-Identifier: BSD-3-Clause

import sys
import subprocess
import sys
import unittest


class TestLapstat(unittest.TestCase):

    def test_lap_times(self):
        result = subprocess.run(
            [sys.executable, "lapstat.py"],
            input="91.122\n90.342\n92.093\n",
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("Fastest lap: 90.34", result.stdout)
        self.assertIn("Slowest lap: 92.09", result.stdout)
        self.assertIn("Average lap: 91.19", result.stdout)

    def test_invalid_input(self):
        result = subprocess.run(
            [sys.executable, "lapstat.py"],
            input="invalid\n",
            capture_output=True,
            text=True
        )

        self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
