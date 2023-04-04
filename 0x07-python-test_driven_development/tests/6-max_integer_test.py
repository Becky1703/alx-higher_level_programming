#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):


    def setUP(self):
        pass


    def Teardown(self):
        pass

    def test_docstring(self):
        self.assertIsNotNone(max_integer.__doc__)
    
    def test_numbers(self):
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-7, -5, 0, 5, 7]), 7)
        self.assertEqual(max_integer([75, 7, 5]), 75)
        self.assertEqual(max_integer([42, 74, 86, 10]), 86)
        self.assertEqual(max_integer([5, 10, 15, 20]), 20)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1]), 1)

    

    def test_string(self):
       self.assertEqual(max_integer(["z", "a"]), "z")



    def test_empty(self):
       self.assertEqual(max_integer([]), None)
       with self.assertRaises(TypeError):
           max_integer(None)


    def test_negative_float(self):
       self.assertEqual(max_integer([-0.9, -23.5, -4.5, -30.1]), -0.9)



    def test_diff_datatypes(self):
       with self.assertRaises(TypeError):
            max_integer([1, "2"])

    def test_list_list(self):
       self.assertEqual(max_integer([[3, 4], [4, 3]]), [4, 3])




if __name__ == "__main__":
    unittest.main()
