import typing

from heapsort import build_max_heap, max_heapify


def max_heap_maximum(a: typing.List[int], heap_size: int) -> typing.Any[int, Exception]:
    """
    Returns the maximum value in a MaxHeap
    :param a: the input MaxHeap
    :param heap_size: the heap size of the given MaxHeap
    :return: the max value
    """
    if heap_size < 1:
        return Exception("Heap Underflow")
    return a[0]


def max_heap_extract_max(a: typing.List[int], heap_size: int) -> int:
    """
    Extracts the maximum element from the heap and returns its value.
    :param a: the input MaxHeap
    :param heap_size: the heap size of the given MaxHeap
    :return: the maximum element in the heap.
    """
    max_elem = max_heap_maximum(a, heap_size)
    a[0] = a[heap_size]
    heap_size -= 1
    max_heapify(a, 0, heap_size)
    return max_elem


def max_heap_increase_key(a: typing.List[int], x: int, k: int):
    if a[x] > k:
        print("Current key is larger than new key")
    a[x] = k
