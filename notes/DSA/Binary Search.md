T- the algorithm
``` python
def binary_search(arr, low, high, x):
    while low <= high :
        mid = low + (high - low) // 2

        # check if x is present at mid
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            # if x is greater, ignore left half
            low = mid + 1
        else:
            high = mid - 1
        return -1

```
**Use cases:**
1) minimize **k** such that condition is true
```python
def binary_search(array):
	def condition(value):
		pass

	left, right = min_search_space, max_seach_space
	while left < right:
		mid = left + (right - left) // 2
		if conidtion(mid):
			right = mid
		else:
			left = mid + 1
	return left
```
In this case we only need to care about the range of the search and the return value. left is the minimal k satisfying the condition.