"""
min-heap is a binary tree that root value is no greater than its left or right child.
starting from 0 and l = 2 * i + 1, r = 2 * i + 2
"""

import unittest
import random
import time

class Heap():

    # build_heap takes O(N) time
    # 1. for a binary tree: leaf# : node# = 2**k : 2**k - 1, thus starting from
    # length//2 to 0 only heapify nodes and skip leaves.
    # 2. Since heapify is O(logN) from level 0 to level k: (2^0 * logk) + (2^1 * (logk-2))
    # + (2^2 * (logk-3)) + ... + (2^k * 1) == O(N)
    @classmethod
    def build_heap(cls,arr):
        length = len(arr)
        for i in range(length // 2, -1, -1):
            Heap.heapify(arr, i)
        return arr

    # Heapify takes O(logN) time
    @classmethod
    def heapify(cls, arr, i):
        length = len(arr)
        l = Heap.left_child(i)
        r = Heap.right_child(i)
        min = i
        if l < length and arr[l] < arr[min]:
            min = l
        if r < length and arr[r] < arr[min]:
            min = r
        if min != i:
            Heap.swap(arr, i, min)
            Heap.heapify(arr, min)

    @classmethod
    def left_child(cls, i):
        return 2 * i + 1

    @classmethod
    def right_child(cls, i):
        return 2 * i + 2

    @classmethod
    def swap(cls, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

class Test(unittest.TestCase):
    def test_empty_heap(self):
        pass

    def test_heap_insert(self):
        arr = [x for x in range(10, -1, -1)]
        arr = Heap.build_heap(arr)
        self.assertEqual([0, 1, 4, 2, 6, 5, 8, 3, 7, 9, 10], arr)


if __name__ == '__main__':
    unittest.main()

