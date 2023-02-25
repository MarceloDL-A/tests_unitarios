
import unittest
import sys
sys.path.insert(0, '/Users/mdelmondes/Desktop/VSCode/meu_projeto')

loader = unittest.TestLoader()
suite = loader.discover('tests')


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite)

