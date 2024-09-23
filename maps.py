#maps

org = [1, 2, 3, 4, 5]

def cube(num):
    return num**3

fin = list(map(cube, org))
print(fin)

#Lambda
flist = list(map(lambda x:x**2, org))
print(flist)

#length
org_list = ["Hello", "world", "freecodecamp"]
fin_list = list(map(len, org_list))
print(fin_list) # [5, 5, 12]

#
base = [1, 2, 3, 4]
power = [1, 2, 3, 4]
result = list(map(pow, base, power))
print(result) # [1, 4, 27, 256]