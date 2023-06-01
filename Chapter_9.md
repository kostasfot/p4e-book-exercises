# Chapter 9: Dictionaries
## Exercise 1 
### Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn't matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary

```python
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
    print('The word is in the file.')
else :
    print('The word is not in the file.')
```
