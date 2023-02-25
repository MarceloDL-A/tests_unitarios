import unittest
import sys
sys.path.insert(0, '/Users/mdelmondes/Desktop/VSCode/meu_projeto')
from multiplica import *


class TestMultiplica(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(multiplica(2, 3), 6)
        self.assertEqual(multiplica(1, -1), -1)
        self.assertEqual(multiplica(1, 1), 1)

if __name__ == '__main__':
    unittest.main()