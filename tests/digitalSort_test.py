from unittest import TestCase, main
from forTests.digitalSort import digitalSort

class DigitalSortCase(TestCase):
    #Positive tests
    def test_sorting_integers_in_ascending_order(self):
        self.assertEqual(digitalSort([4, 5, 1, 6, 8]), [1, 4, 5, 6, 8])

    #Boundary tests
    def test_sorting_array_with_minimum_possible_integer_values(self):
        self.assertEqual(digitalSort([]), [])

    def test_sorting_array_with_only_identical_elements(self):
        self.assertEqual(digitalSort([1]), [1])

    # Special case tests
    def test_sorting_already_sorted_array_in_ascending_order(self):
        self.assertEqual(digitalSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_sorting_already_sorted_array_in_descending_order(self):
        self.assertEqual(digitalSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_sorting_array_with_duplicate_values(self):
        self.assertEqual(digitalSort([3, 7, 2, 3, 0, 3, 3, 3, 3, 3, 2]), [0, 2, 2, 3, 3, 3, 3, 3, 3, 3, 7])

    #Negative tests
    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            digitalSort("abracadabra")
        # проверка текста сообщения об ошибке
        self.assertEqual("Выражение на вход должно являться массивом целых чисел", e.exception.args[0])

    def test_float(self):
        with self.assertRaises(ValueError) as e:
            digitalSort(12.578)
        # проверка текста сообщения об ошибке
        self.assertEqual("Выражение на вход должно являться массивом целых чисел", e.exception.args[0])

    def test_floats_array(self):
        with self.assertRaises(ValueError) as e:
            digitalSort([2.5, 1.0, 0.5, 3.0])
        # проверка текста сообщения об ошибке
        self.assertEqual("Выражение на вход должно являться массивом целых чисел", e.exception.args[0])

    def test_strings_array(self):
        with self.assertRaises(ValueError) as e:
            digitalSort(['apple', 'banana', 'pear', 'cherry'])
        # проверка текста сообщения об ошибке
        self.assertEqual("Выражение на вход должно являться массивом целых чисел", e.exception.args[0])






if __name__ == "__main__":
    main()