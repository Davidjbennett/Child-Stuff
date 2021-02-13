import unittest
from sort import selection_sort, insertion_sort, mergesort, quicksort, is_sorted
from random import seed, sample
from time import perf_counter

class TestSortTiming(unittest.TestCase):
    def test_sort_times(self):
        data_size = 1000
        seed(42)
        data = sample(range(data_size * 3), k=data_size)

        # selection sort        
        test = data.copy()
        start = perf_counter()
        test = selection_sort(test)
        selection_elapsed_time = perf_counter() - start
        self.assertTrue(is_sorted(test))


        # insertion sort        
        test = data.copy()
        start = perf_counter()
        test = insertion_sort(test)
        insertion_elapsed_time = perf_counter() - start
        self.assertTrue(is_sorted(test))

        # merge sort        
        test = data.copy()
        start = perf_counter()
        test = mergesort(test)
        merge_elapsed_time = perf_counter() - start
        self.assertTrue(is_sorted(test))

        # quick sort        
        test = data.copy()
        start = perf_counter()
        test = quicksort(test)
        quick_elapsed_time = perf_counter() - start
        self.assertTrue(is_sorted(test))

        # tim sort        
        test = data.copy()
        start = perf_counter()
        test.sort()
        tim_elapsed_time = perf_counter() - start

        self.assertLess(merge_elapsed_time, insertion_elapsed_time)
        self.assertLess(quick_elapsed_time, selection_elapsed_time)
        self.assertLess(tim_elapsed_time, merge_elapsed_time)

class TestIsSorted(unittest.TestCase):
    def test_sorted_list(self):
        data_size = 1000
        seed(42)
        orig_data = sample(range(data_size * 3), k=data_size)

        self.assertFalse(is_sorted(orig_data))
        test_data = selection_sort(orig_data.copy())
        self.assertTrue(is_sorted(test_data))
        test_data = insertion_sort(orig_data.copy())
        self.assertTrue(is_sorted(test_data))
        test_data = mergesort(orig_data.copy())
        self.assertTrue(is_sorted(test_data))
        test_data = quicksort(orig_data.copy())
        self.assertTrue(is_sorted(test_data))

class TestParameterTypes(unittest.TestCase):
    def test_parameters(self):
        self.assertRaises(ValueError, mergesort, "cat")
        self.assertRaises(ValueError, quicksort, "cat")
        self.assertRaises(ValueError, insertion_sort, "cat")
        self.assertRaises(ValueError, selection_sort, "cat")
        self.assertRaises(ValueError, is_sorted, [1,2,"cat",4])

class TestCodingStandards(unittest.TestCase):
    def test_code_quality(self):
        from pylint import epylint as lint
        import glob
        for file_name in glob.glob('*.py'):
            if file_name[:5] != "test_" and file_name != "recursioncounter.py":
                (pylint_stdout, _) = lint.py_run(file_name, return_std=True)
                output = pylint_stdout.getvalue()
                offset = output.rfind(" been rated at ")
                if offset != -1:
                    output = output[offset:]
                    end = output.find('/')
                    output = output[15:end]
                    score = float(output)
                    self.assertGreaterEqual(score, 8.5)
