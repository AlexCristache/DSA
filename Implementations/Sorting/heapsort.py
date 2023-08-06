import math
import typing


def right(i: int) -> int:
    """
    Returns the value of the right child of node at index i in a MaxHeap
    :param i: index of the node
    :return: the value of the right child
    """
    return 2 * (i + 1)


def left(i: int) -> int:
    """
    Returns the value of the left child of node at index i in a MaxHeap
    :param i: index of the node
    :return: the value of the left child
    """
    return 2 * i + 1


def parent(i: int) -> int:
    """
    Returns the value of the parent of node at index i in a MaxHeap
    :param i: index of the node
    :return: the value of the parent
    """
    return math.floor(i/2)


def max_heapify(a: typing.List[int], i: int, heap_size: int) -> typing.List[int]:
    """
    Ensures that the tree with root at index i is a MAX-HEAP. Assume a.heap_size == len(a)
    :param a: the array representing the MaxHeap
    :param i: the index of the element considered root
    :param heap_size: the length of the current MaxHeap
    :return: the array A which now satisfies the condition to be a MaxHeap
    """
    l = left(i)
    r = right(i)
    if l <= heap_size and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        aux = a[i]
        a[i] = a[largest]
        a[largest] = aux
        max_heapify(a, largest, heap_size)
    return a


def build_max_heap(a: typing.List[int], n: int) -> typing.List[int]:
    """
    Makes sure that the array a is a MaxHeap by taking a bottom-up approach.
    :param a: the input array
    :param n: the heap size
    :return: the array arranged as a MaxHeap
    """
    heap_size = len(a) - 1
    for i in range(math.floor(n/2), -1, -1):
        max_heapify(a, i, heap_size)
    return a


def heapsort(a: typing.List[int], n: int, heap_size) -> typing.List[int]:
    build_max_heap(a, n)
    for i in range(n, 0, -1):
        aux = a[0]
        a[0] = a[i]
        a[i] = aux
        heap_size -= 1
        max_heapify(a, 0, heap_size)
    return a


if __name__ == "__main__":
    input_array = [16, 1, 10, 8, 7, 9, 3, 2, 4, 14]
    # out_array = max_heapify(input_array, 1)
    # print(out_array)
    # input_array.sort()
    print(f"converting the array {input_array} into a max heap:")
    # out_heap = build_max_heap()
    out = heapsort(input_array, len(input_array) - 1, len(input_array) - 1)
    print(out)
