# Input list of tuples
word_counts = [
    ('apple', 4),
    ('banana', 2),
    ('apple', 3),
    ('orange', 5),
    ('banana', 1)
]

# Initialize an empty dictionary to store word frequencies
frequency_counter = {}

# Process each tuple in the list
for word, count in word_counts:
    if word in frequency_counter:
        frequency_counter[word] += count
    else:
        frequency_counter[word] = count

print(frequency_counter)
