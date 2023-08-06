import typing


def insertion_sort(a: typing.List[int], n: int) -> typing.List[int]:
    """
    Implements the insertion sort algorithm.
    :param a: the array
    :param n: the number of the elements to be sorted
    :return: the sorted array
    """
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    return a


if __name__ == "__main__":
    initial_array = [2, 1, 3]
    out = insertion_sort(initial_array, len(initial_array))
    print(out)