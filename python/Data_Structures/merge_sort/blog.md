# Merge Sort

This sorting algorithm takes less time than insertion sorting and of course than bubble sorting.

The idea behind it is that the array is divided from the middle recursively into left and right parts until the array are no longer dividable (has only one item), then within each array(left and right) the values are compared and sorted and at the end the two arrays are compared and merged.  

## example:
![img](../../assets/merge-sort/mergesort1.png)

### step 1:
the array is divided from the middle into left and right arrays.
![img](../../assets/merge-sort/mergesort2.png)

### step 2:
the two arrays are again and again divided from the middle until they have one item only.
![img](../../assets/merge-sort/mergesort3.png)

### step 3:
each array values are internally compared and sorted.
![img](../../assets/merge-sort/mergesort4.png)

### step 4:
Now, the left and right arrays are compared value by value as shown below and the smaller value is added to the array.      
![img](../../assets/merge-sort/mergesort5.png)

### step 5:
![img](../../assets/merge-sort/mergesort6.png)

### step 6:
![img](../../assets/merge-sort/mergesort7.png)

### step 7:
![img](../../assets/merge-sort/mergesort8.png)

### step 8:
![img](../../assets/merge-sort/mergesort9.png)

### step 9:
the last step is to add the remaining values from the right array to the main array.
![img](../../assets/merge-sort/mergesort10.png)
