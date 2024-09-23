d = {'DOG' : 'has a tail and goes woof!',
'CAT' : 'says meow',
'MOUSE' : 'chased by cats'}

word = input('Enter a word: ').upper()
print('The definition is:', d[word])

numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

points = {'A':1, 'B':3, 'C':3, 'D':2, 'E':1, 'F':4, 'G':2,
'H':4, 'I':1, 'J':8, 'K':5, 'L':1, 'M':3, 'N':1,
'O':1, 'P':3, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':1,
'V':4, 'W':4, 'X':8, 'Y':4, 'Z':10}

#do not forget to index digits
score = sum([points[c] for c in word])

total = 0
for c in word:
    total += points[c]

print(total)

import random
def shuffle(deck):
    random.shuffle(deck)
    return deck

deck = [{'num':i, 'suit': c}
        for c in ['spades', 'clubs', 'hearts', 'diamonds']
        for i in range(2, 15)]

sc = shuffle(deck)
for card in sc:
    print(card)

D = {'A':100, 'B':200, 'C':100}
L = [x[0] for x in d.items() if x[1] == 100]
print(L)