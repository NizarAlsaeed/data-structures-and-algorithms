# Challenge Summary
<!-- Description of the challenge -->
create a blog article that shows the step-by-step output after each iteration through some sort of visual.
then code a working, tested implementation of Merge Sort based on the pseudocode provided.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![img](../../assets/merge-sort/mergesort3.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Applied the pseudocode provided with the challenge
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

BigO(n log (n))

## Solution
<!-- Show how to run your code, and examples of it in action -->

```python
import math

def mergesort(arr:list):
    n = len(arr)

    if n > 1:
      mid = math.ceil(n/2)
      left = arr[0:mid]
      right = arr[mid:]
      # sort the left side
      mergesort(left)
      # sort the right side
      mergesort(right)
      # merge the sorted left and right sides together
      return merge(left, right, arr)

def merge(left:list, right:list, arr:list):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left):
      arr[k]=left[i]
      i=i+1
      k=k+1

    while j < len(right):
      arr[k]=right[j]
      j=j+1
      k=k+1
    return arr


print(mergesort([8,4,23,42,16,15]))

# [4,8,15,16,23,42]
```
