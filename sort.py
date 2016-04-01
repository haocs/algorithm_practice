import unittest
import time
import random

from structures.heap import Heap

class Sort():
    # assume ascending
    def _swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

    def selection_sort(self, unsorted_arr):
        arr = unsorted_arr[::]
        length = len(arr)
        for i in range(0, length):
            min_idx = i
            for j in range(i, length):
                if arr[j] < arr[min_idx]:
                    self._swap(arr, min_idx, j)
        return arr

    def insertion_sort(self, unsorted_arr):
        # the way we sorting cards
        arr = unsorted_arr[::]
        length = len(arr)
        for i in range(1, length):
            # i will be assigned new value in each loop
            while i > 0 and arr[i] < arr[i-1]:
                self._swap(arr, i, i-1)
                i -= 1
        return arr

    def shell_sort(self, unsorted_arr, h):
        arr = unsorted_arr[::]
        length = len(arr)
        while h > 0:
            for i in range(0, h):
                for j in range(i, length, h):
                    while j > i and arr[j] < arr[j - h]:
                        self._swap(arr, j, j-h)
                        j -= h
            h /= 2
        return arr

    # can also do in-place sort
    def merge_sort(self, unsorted_arr):

        def divide(arr):
            length = len(arr)
            if length < 2:
                return arr
            left = divide(arr[0:length/2])
            right = divide(arr[length/2:])
            return merge(left, right)

        def merge(arr1, arr2):
            out_a = []
            l1, l2 = len(arr1), len(arr2)
            i, j = 0, 0
            while i < l1 and j < l2:
                if arr1[i] < arr2[j]:
                    out_a.append(arr1[i])
                    i += 1
                else:
                    out_a.append(arr2[j])
                    j += 1
            if i < l1:
                out_a.extend(arr1[i::])
            if j < l2:
                out_a.extend(arr2[j::])
            return out_a

        return divide(unsorted_arr)

    def quick_sort(self, unsorted_arr):
        def get_pivot(arr, l, r):
            return r

        def partition(arr, l, r):
            p = get_pivot(arr, l, r)
            self._swap(arr, p, r)

            i, j = l-1, l
            while j <= r:
                if arr[j] <= arr[p]:
                    i += 1
                    self._swap(arr, i, j)
                j += 1

            return i

        def quicksort(arr, l, r):
            if (r - l) < 1:
                return

            j = partition(arr, l, r)

            quicksort(arr, l, j-1)
            quicksort(arr, j+1, r)

        arr = unsorted_arr[::]
        quicksort(arr, 0, len(arr)-1)
        return arr

    def heap_sort(self, unsorted_arr):
        arr = unsorted_arr[::]
        arr = Heap.build_heap(arr)
        res = []
        while len(arr) > 0:
           res.append(arr[0])
           Heap.swap(arr, 0, len(arr) - 1)
           arr = arr[:-1]
           Heap.heapify(arr, 0)
        return res

def profile(loop):
    arr = [int(random.random() * 1000) for x in range(0, 500)]
    # arr = [x for x in range(100, 0, -1)]

    s = Sort()
    mills = 10 ** 6
    start = time.time() * mills
    for i in range(0, loop):
        s.selection_sort(arr)
    print(str(time.time() * mills - start))

    start = time.time() * mills
    for i in range(0, loop):
        s.insertion_sort(arr)
    print(str(time.time() * mills - start))

    start = time.time() * mills
    for i in range(0, loop):
        s.shell_sort(arr, 100)
    print(str(time.time() * mills - start))

    start = time.time() * mills
    for i in range(0, loop):
        s.merge_sort(arr)
    print(str(time.time() * mills - start))

    start = time.time() * mills
    for i in range(0, loop):
        s.quick_sort(arr)
    print(str(time.time() * mills - start))

    start = time.time() * mills
    for i in range(0, loop):
        s.heap_sort(arr)
    print(str(time.time() * mills - start))


class Test(unittest.TestCase):
    def test_empty_arr(self):
        pass

    def test_selection_sort(self):
        arr = [1, 2, 4, 7, 6, 3, 3, -3, 3, 3, 5,4,54,3,345,7,22,33,33,44]
        s = Sort()
        self.assertEqual(sorted(arr), s.selection_sort(arr))

    def test_insertion_sort(self):
        arr = [1, 2, 4, 7, 6, 3, 3, -3, 3, 3, 5,4,54,3,345,7,22,33,33,44]
        s = Sort()
        self.assertEqual(sorted(arr), s.insertion_sort(arr))

    def test_shell_sort(self):
        arr = [1, 2, 4, 7, 6, 3, 3, -3, 3, 3, 5,4,54,3,345,7,22,33,33,44]
        s = Sort()
        self.assertEqual(sorted(arr), s.shell_sort(arr, len(arr)/2))

    def test_merge_sort(self):
        arr = [1, 2, 4, 7, 6, 3, 3, -3, 3, 3, 5,4,54,3,345,7,22,33,33,44]
        s = Sort()
        self.assertEqual(sorted(arr), s.merge_sort(arr))

    def test_quick_sort(self):
        arr = [1, 2, 4, 7, 6, 3, 3, -3, 3, 3, 5,4,54,3,345,7,22,33,33,44]
        s = Sort()
        self.assertEqual(sorted(arr), s.quick_sort(arr))

    def test_heap_sort(self):
        arr = [1, 2, 4, 7, 6, 3, 3, -3, 3, 3, 5,4,54,3,345,7,22,33,33,44]
        s = Sort()
        self.assertEqual(sorted(arr), s.heap_sort(arr))

if __name__ == '__main__':
    # unittest.main()
    profile(100)

