from matplotlib import pyplot as plt

from main import heap_sort
from timeit import repeat
import random


def merge_sort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        merge_sort(L)
 
        # Sorting the second half
        merge_sort(R)
 
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

def repeat_wrapper(algorithm, arr):
    return repeat(
        stmt = f"{algorithm}({arr})",

        setup = f"from __main__ import \
                {algorithm}",

                repeat = 1,
                number = 10)
 
 
samples = 3000
x = list(range(samples))
yms = []
yhs = []
for i in range(samples):
    arr = random.sample(range(-samples, samples), i)
    tms = repeat_wrapper("merge_sort", arr)
    ths = repeat_wrapper("heap_sort", arr)


    yms.append(tms)
    yhs.append(ths)
    # flush
    print (100*i/samples, "%")

plt.plot(x,yms)
plt.plot(x,yhs)
plt.show()

 
# This code is contributed by Mayank Khanna
