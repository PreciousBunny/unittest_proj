import unittest
from utils.arrs import get, my_slice


class TestArray(unittest.TestCase):
    def setUp(self):
        self.__array = [1, 2, 3, 4, 5]

    def test_get(self):
        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])

    def test_my_slice_empty(self):
        self.assertEqual(my_slice([]), [])

    def test_my_slice_start_opening(self):
        self.assertEqual(my_slice(self.__array, start=3), [4, 5])

    def test_my_slice_reverse_start_opening(self):
        self.assertEqual(my_slice(self.__array, start=-3), [3, 4, 5])

    def test_my_slice_reverse_start_opening_and_another_arguments(self):
        self.assertEqual(my_slice(self.__array, start=-3, end=-1), [3, 4])

    def test_my_slice_basis_start(self):
        self.assertEqual(my_slice(self.__array, start=-len(self.__array) - 1), my_slice(self.__array))

