"""
min-heap is a binary tree that root value is no greater than its left or right child.

heap interface:
    insert()
    heapify()
    pop()
"""

import unittest
import random
import time

class Heap():
    @classmethod
    def build_heap(cls,arr):
        length = len(arr)
        for i in range(length // 2, -1, -1):
            Heap.heapify(arr, i)
        return arr

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
    def parent(cls, arr, i):
        pass
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
        self.assertEqual([0, 1, 5, 4, 2, 9, 6, 10, 7, 8, 3], arr)


if __name__ == '__main__':
    unittest.main()

