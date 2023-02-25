import unittest
import sys
sys.path.insert(0, '/Users/mdelmondes/Desktop/VSCode/meu_projeto')
from subtrai import *


class TestSubtrai(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(subtrai(2, 3), -1)
        self.assertEqual(subtrai(1, -1), 2)
        self.assertEqual(subtrai(1, 1), 0)

if __name__ == '__main__':
    unittest.main()
