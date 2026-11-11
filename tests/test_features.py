import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class ExpenseTests(unittest.TestCase):
    def test_add_and_total(self):
        with tempfile.TemporaryDirectory() as temp:
            result = subprocess.run(
                [sys.executable, str(ROOT / "main.py")],
                input="1\nFood\n125\n3\n4\n",
                text=True, capture_output=True,
                cwd=temp, timeout=10
            )
            self.assertEqual(result.returncode, 0)
            self.assertIn("125", result.stdout)
            self.assertTrue((Path(temp) / "expenses.db").exists())
