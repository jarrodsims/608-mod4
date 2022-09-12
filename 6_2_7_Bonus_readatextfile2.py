# 6_2_7_Bonus_readatextfile.py
"""Read a text file and count unique words."""

f = open("C:\\Users\\jarro\\OneDrive\\Documents\\44-608\\608-mod4\\preamble.txt", "r")
text = f.read()

word_counts = {}

# count occurrences of each unique word
for word in text.split():
    if word in word_counts: 
        word_counts[word] += 1  # update existing key-value pair
    else:
        word_counts[word] = 1  # insert new key-value pair

print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))
print('Jarrod Sims')