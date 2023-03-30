from unittest import TestCase, main
from forTests.bubbleSort import bubbleSort

class BubbleSortCase(TestCase):
    #Positive tests
    def test_sorting_integers_in_ascending_order(self):
        self.assertEqual(bubbleSort([4, 2, 1, 6, 7]), [1, 2, 4, 6, 7])

    def test_sorting_strings_in_ascending_order(self):
        self.assertEqual(bubbleSort(['apple', 'banana', 'pear', 'cherry']), ['apple', 'banana', 'cherry', 'pear'])

    def test_sorting_floating_point_numbers_in_ascending_order(self):
        self.assertEqual(bubbleSort([2.5, 1.0, 0.5, 3.0]), [0.5, 1.0, 2.5, 3.0])

    #Boundary tests
    def test_sorting_array_with_minimum_possible_integer_values(self):
        self.assertEqual(bubbleSort([]), [])

    def test_sorting_array_with_only_identical_elements(self):
        self.assertEqual(bubbleSort([1]), [1])

    # Special case tests
    def test_sorting_already_sorted_array_in_ascending_order(self):
        self.assertEqual(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sorting_already_sorted_array_in_descending_order(self):
        self.assertEqual(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sorting_array_with_duplicate_values(self):
        self.assertEqual(bubbleSort([3, 7, 2, 3, 0, 3, 3, 3, 3, 3, 2]), [0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 7])

    #Negative tests
    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            bubbleSort("abracadabra")
        # проверка текста сообщения об ошибке
        self.assertEqual("Выражение на вход должно являться массивом", e.exception.args[0])

    def test_float(self):
        with self.assertRaises(ValueError) as e:
            bubbleSort(12.578)
        # проверка текста сообщения об ошибке
        self.assertEqual("Выражение на вход должно являться массивом", e.exception.args[0])



if __name__ == "__main__":
    main()