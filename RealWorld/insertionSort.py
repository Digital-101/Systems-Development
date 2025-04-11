def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

sortArr = [53,90,47,28,4,19,82,70,64]
print(insertion_sort(sortArr))