def insertion_sort(arr: list):

    for i in range(len(arr)):

        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp

    return arr

if __name__ == '__main__':
    print(insertion_sort([8, 4, 2, 3, 4, 2, 16, 15]))
