import unittest


def is_sorted_ascending(test_list: list):
    return all(test_list[i] <= test_list[i+1] for i in range(len(test_list)-1))


class TestSortedAscending(unittest.TestCase):
    def test_sorted_list(self):
        example_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # example_list_1 = [5, 3, 7, 4, 1, 5, 8, 9, 2]
        print(f"Posortowana lista: {example_list_1}")
        self.assertTrue(is_sorted_ascending(example_list_1))

    def test_unsorted_list(self):
        # example_list_1 = [1, 2, 3]
        example_list_1 = [5, 3, 1, 6, 8, 9, 7]
        print(f"Nieposortowana lista: {example_list_1}")
        self.assertFalse(is_sorted_ascending(example_list_1))


if __name__ == "__main__":
    unittest.main()
