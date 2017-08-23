import unittest
from quicksort import quicksort

class TestQuickSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(quicksort([]), [])

    def test_simple_sorted_list(self):
        self.assertEqual(quicksort([1,2,3,4]), [1,2,3,4])

    def test_simple_unsorted_list(self):
        self.assertEqual(quicksort([2,3,1,5,6]), [1,2,3,5,6])

    def test_reverse_sorted_list(self):
        self.assertEqual(quicksort([5,4,3,2,1]), [1,2,3,4,5])

    def test_long_unsorted_list(self):
        long_unsorted_list = [12,3,4,12,4,35,6,7,23,4,5,6,46,43,1,1,111,2,3,4,535,6,53,45,2,21,4,52,3,4,5,6,345,32,42]
        self.assertEqual(quicksort(long_unsorted_list), sorted(long_unsorted_list))

if __name__ == '__main__':
    unittest.main()
