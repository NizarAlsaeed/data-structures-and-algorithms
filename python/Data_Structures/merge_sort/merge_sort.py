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

if __name__=='__main__':
    print(mergesort([8,4,23,42,16,15]))
