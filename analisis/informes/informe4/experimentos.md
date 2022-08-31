# Heap Sort

## Experimentos

### Comparación con MergeSort

```python
import random
# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
# Code to print the list
 
 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
samples = 300
for i in range(samples):
  arr = random.sample(range(-samples, samples) samples)
  mergeSort(arr)
 
# This code is contributed by Mayank Khanna
```

*Results:*
```
Traceback (most recent call last):
  File "/tmp/mdeval//experimentosmd_7_66.py", line 55, in <module>
    arr = random.sample(range(-samples, samples, samples))
TypeError: Random.sample() missing 1 required positional argument: 'k'
```

### Comparación con QuickSort
