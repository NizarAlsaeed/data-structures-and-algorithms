# Quick Sort
it is a popular and very useful sorting algorithm, it's idea is to pick up a random value from the array, called (pivot), and place all values lower than the pivot on the left, and all the greater values on the right of the pivot, and those two new arrays are again partitioned with the same process until the arrays are no longer partitionable. then the values are compared and placed again to form a sorted array.


### step1:
first of all, we will arbitrarily choose the last item in the array as the pivot.

![img](../../assets/qsort1.png)

### step2:
then, we compare the other values with the pivot and place whatever is lower than it to the left in a new array and the greater values o the right as shown below.

![img](../../assets/qsort2.png)

### step3:
repeat the process again on the left and right arrays

![img](../../assets/qsort3.png)

### step4:

![img](../../assets/qsort4.png)

### step5:
now we move to the back by combining the left and right values to the pivot as shown on the following steps.

![img](../../assets/qsort5.png)

### step6:
![img](../../assets/qsort6.png)

### step7:
![img](../../assets/qsort7.png)

### step8:
and we are done, the array is now correctly sorted.

![img](../../assets/qsort8.png)


## run-time:

from the algorithm structure it can be noticed that the Time complexity may reach to  O(n²) in the worst case when the array is initially sorted, but in good cases the complexity goes to O(n log n) .
