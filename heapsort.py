def heapify(arr, n, i):
    largest = i
    l = 2*i + 1 #left
    r = 2*i + 2 #right

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r
    
    #change root, if needed
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) #swap

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    #one by one extract elements
    for i in range(n-1,0,-1):
        (arr[i], arr[0]) = (arr[0], arr[i]) #swap

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print('Sorted array is')
for i in range(n):
    print(arr[i])