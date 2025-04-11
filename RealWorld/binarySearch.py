def binary_search(sortedArray, X):
    left, right = 0, len(sortedArray) - 1
    while left <= right:
        mid = (left + right) // 2
        if sortedArray[mid] == X:
            return mid
        elif sortedArray[mid] < X:
            left = mid + 1
        else:
            right = mid -1
    return -1

searchArr = [13,22,28,43,56,61,72,90,94]
print(binary_search(searchArr, 61))