def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + quick_sort(middle) + quick_sort(right)

sortArr = [53,90,47,28,4,19,82,70,64]
print(quick_sort(sortArr))
