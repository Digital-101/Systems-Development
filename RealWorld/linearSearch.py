def linear_search(array, X):
    for i in range(0, len(array)):
        if array[i] == X:
            return True
        
searchArr = [13,22,28,43,56,61,72,90,94]
print(linear_search(searchArr, 43))

############
def linearSearch(array, X):
    for index, value in enumerate(array):
        if value == X:
            return index

searchArr = [13,22,28,43,56,61,72,90,94]
print(linearSearch(searchArr, 72))