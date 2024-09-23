heights = (7.3, 5.3, 12.8, 6.2, 9)
girls_height = (5.2, 4.7)

#Index
print(heights[0])

#Slice
print(heights[1:4])

# Membership
6.2 in heights

def add_height():
    new_height = (6, 4.9)
    return (heights + new_height)

def duplicate_height():
    return (girls_height * 2)

#Comparison
if heights != girls_height:
    print('True')
