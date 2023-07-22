def quickSort(array, low, high):
    if high <= low:
        return array
    j = low - 1
    last = array[high]
    for i in range(low, high + 1):
        if array[i] <= last:
            j += 1
            if i > j:
                array[i], array[j] = array[j], array[i]
    quickSort(array, low, j - 1)
    quickSort(array, j + 1, high)


input_array = [3, 2, 5, 0, 1, 8, 7, 6, 9, 4]
quickSort(input_array, 0, len(input_array) - 1)
print(input_array)
