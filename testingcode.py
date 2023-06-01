fhand = open('exercise-files/words.txt')
word_dict = dict()
count = 0

for line in fhand :
    words = line.split()
    for word in words :
        count = count + 1
        if word in word_dict :
            continue
        else :
            word_dict[word] = count
            
check = input('Enter a word to check: ')

if check in word_dict :
    print(f'The word "{check}" is in the file.')
else :
    print(f'The word "{check}" is not in the file.')