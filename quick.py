#always check your code
def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + quick_sort(middle) + quick_sort(right)

array = [20,78,12,9,3,31]
print(quick_sort(array))