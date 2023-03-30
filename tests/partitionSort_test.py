from unittest import TestCase, main
from forTests.partitionSort import partitionSort

class DigitalSortCase(TestCase):
    #Positive tests
    def test_sorting_integers_in_ascending_order(self):
        self.assertEqual(partitionSort([9, 6, 1, 5, 3, 4, 8, 7, 2, 0], 3, 9), ([9, 6, 1, 2, 3, 4, 0, 5, 7, 8], 7))

    def test_sorting_strings_in_ascending_order(self):
        self.assertEqual(partitionSort(["a", "d", "dad", "wa", "da"], 2, 3), (['a', 'd', 'dad', 'wa', 'da'], 2))

    def test_sorting_floats_in_ascending_order(self):
        self.assertEqual(partitionSort([0.2, 1.1, 4.5, 0.1, 7.3, 0.02], 2, 5), ([0.2, 1.1, 0.02, 0.1, 4.5, 7.3], 4))

    #Boundary tests
    def test_sorting_array_with_minimum_possible_integer_values(self):
        self.assertEqual(partitionSort([], 9, 8), [])

    def test_sorting_array_with_only_identical_elements(self):
        self.assertEqual(partitionSort([1], 2, 6), [1])

    # Special case tests
    def test_sorting_already_sorted_array_in_ascending_order(self):
        self.assertEqual(partitionSort([1, 2, 3, 4, 5], 0, 4), ([1, 2, 3, 4, 5], 0))

    def test_sorting_already_sorted_array_in_descending_order(self):
        self.assertEqual(partitionSort([5.2, 4.45, 3.21, 2.9, 1.76], 0, 4), ([1.76, 4.45, 3.21, 2.9, 5.2], 4))

    def test_sorting_array_with_duplicate_values(self):
        self.assertEqual(partitionSort([3, 7, 2, 3, 0, 3, 3, 3, 3, 3, 2], 0, 8), ([3, 3, 2, 3, 0, 3, 3, 3, 7, 3, 2], 5))

    #Negative tests
    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            partitionSort("abracadabra", 0, 1)
        # проверка текста сообщения об ошибке
        self.assertEqual("На вход должны идти массив элементов одного типа и 2 целых положительных числа", e.exception.args[0])

    def test_float(self):
        with self.assertRaises(ValueError) as e:
            partitionSort([5.2, 4.45, 3.21, 2.9, 1.76], -4, -10)
        # проверка текста сообщения об ошибке
        self.assertEqual("На вход должны идти массив элементов одного типа и 2 целых положительных числа", e.exception.args[0])

    def test_float(self):
        with self.assertRaises(ValueError) as e:
            partitionSort(12.578, 4, 10)
        # проверка текста сообщения об ошибке
        self.assertEqual("На вход должны идти массив элементов одного типа и 2 целых положительных числа", e.exception.args[0])


if __name__ == "__main__":
    main()