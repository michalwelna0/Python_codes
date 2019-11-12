# Pozostaw ten plik pusty, ew. wykorzystaj do własnych testów.
# Michał Wełna 302935
import unittest, sort, random

class TestAlgorythms(unittest.TestCase):
    def test_Bubblesort(self):
        lst = [10,3,4,1,6,8,9,2,5,7]
        result = ([x for x in range(1,11)], 42)
        self.assertEqual(sort.bubblesort(lst), result)

    def test_Quicksort(self):
        lst2 = [5,4,6,8,10,2,7,1,9,3]
        self.assertEqual(sort.quicksort(lst2), [y for y in range(1,11)])

if __name__ == '__main__':
    unittest.main()