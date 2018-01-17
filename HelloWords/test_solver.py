import unittest
from Solver import solver

class TestSolver(unittest.TestCase):

    def test_negative_discr(self):
        s = solver

        self.assertRaises(Exception, s.demo, 2, 1, 2)

    def test_something(self):

        self.assertRaises(True, False)



if __name__ == '__main__':
    unittest.main()


