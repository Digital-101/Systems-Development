#For exchange of items that are far aprt
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j=i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j-gap]
                j-=gap
            arr[j] = temp
        gap //=2
    return arr

array = [12, 34, 54, 2, 3]
print(shell_sort(array))