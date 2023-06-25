import string

counts = 0
dict_counts = dict()
lst = list()

fname = input('Enter file path: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File not found, setting random file.')
    fhand = open('exercise-files/romeo-full.txt')
    
for line in fhand:
    line = line.rstrip()
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()

    for word in words:
        for letter in word:
            counts = counts + 1
            if letter not in dict_counts:
                dict_counts[letter] = 1
            else:
                dict_counts[letter] += 1

for key, val in list(dict_counts.items()):
    lst.append((val / counts, key))

lst.sort(reverse=True)

for key, val in lst:
    print(key, val)