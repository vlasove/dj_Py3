"""
В этом модуле содержатся тесты для funcs.py
"""

import unittest
import funcs 


class TestFuncs(unittest.TestCase):
    def abcs(self):
        pass
    def test_add(self):
        self.assertEqual(funcs.add(2, 3) , 5)
        self.assertEqual(funcs.add(0, 10), 10)

    def test_sub(self):
        self.assertEqual(funcs.sub(10, 2), 8)
        self.assertEqual(funcs.sub(0, 10), -10) 

    def test_mult(self):
        self.assertEqual(funcs.mult(10,10), 100) 


if __name__ == "__main__":
    unittest.main()