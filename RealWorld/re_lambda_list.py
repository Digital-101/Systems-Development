#1. ######
#Regular Expressions are a valuable tool for finding patterns in string
import re

phone = "072-123-1022"
mail = "johndoe@example.com"

match = re.search(r'\d{3}-\d{3}-\d{4}',phone)
ematch = re.search(r'\w+@\w+\.\w+', mail)

if match and ematch:
    print('Phone = ',match.group())
    print('Mail = ',ematch.group())

else:
    print('None')

#2. #######
#lambda functions also referred to as anonymous functions are used to create small, temporary functions
# filtering, mapping, sorting
square = lambda x:x**2
print(square(5))

#3. #######
#list comprehension 
numbers = [1, 2, 3, 4, 5]
cubes = [x ** 3 for x in numbers]
print(cubes)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]
print(flat)

#4. ########
#Decorators provide a way to change the behaviour of functions or classes without altering original code
#@symbol
import time
def time_is(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:4f} seconds")
        return result
    return wrapper

@time_is
def slow_function():
    time.sleep(1)
slow_function()

#4. ########
#Generators allows you to create iterators which are objects that generate a sequence of values
#suitable for large datasets
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci()
for i in range(10):
    print(next(fib))

#Hypothesis Testing
from scipy.stats import ttest_ind

group1 = [1,2,3,4,5]
group2 = [6,7,8,9,10]
stat, p = ttest_ind(group1, group2)
print("Test Statistic:",stat)
print("P-Vakue:",p)