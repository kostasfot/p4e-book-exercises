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

## Exercise 2
### Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with 'From', then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

```python
fname = input("Enter file name: ")

try :
    fhand = open(fname)
except :
    print("File cannot be opened:", fname)
    print('Setting file to mbox-short.txt')
    fhand = open('exercise-files/mbox-short.txt')

counts = dict()
    
for line in fhand :
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : 
        continue
    else :
        if words[2] not in counts :
            counts[words[2]] = 1
        else :
            counts[words[2]] += 1
            
print(counts)
```

## Exercise 3
### Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

```python
fname = input("Enter file name: ")

try :
    fhand = open(fname)
except :
    print("File cannot be opened:", fname)
    print('Setting file to mbox-short.txt')
    fhand = open('exercise-files/mbox-short.txt')

counts = dict()
    
for line in fhand :
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : 
        continue
    else :
        if words[1] not in counts :
            counts[words[1]] = 1
        else :
            counts[words[1]] += 1
            
print(counts)
```

## Exercise 4
### Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum and minimum loop to find who has the most messages and print how many messages the person has.

```python
fname = input("Enter file name: ")

try :
    fhand = open(fname)
except :
    print("File cannot be opened:", fname)
    print('Setting file to mbox-short.txt')
    fhand = open('exercise-files/mbox-short.txt')

counts = dict()
    
for line in fhand :
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : 
        continue
    else :
        if words[1] not in counts :
            counts[words[1]] = 1
        else :
            counts[words[1]] += 1
            
mxcount = None
mxkey = None

for key in counts:
    if mxcount is None or counts[key] > mxcount :
        mxcount = counts[key]
        mxkey = key

print(mxkey, mxcount)
```

## Exercise 5 
### This program records the domain name (instead of the address) where the message was sent from instead of who the mail came form (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

```python
import string

fname = input("Enter file name: ")

try :
    fhand = open(fname)
except :
    print("File cannot be opened:", fname)
    print('Setting file to mbox-short.txt')
    fhand = open('exercise-files/mbox-short.txt')

counts = dict()
    
atpos = None
domain = None
    
for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' : 
        continue
    atpos = words[1].find('@')
    domain = words[1][atpos+1 :]
    
    if domain not in counts :
        counts[domain] = 1
    else:
        counts[domain] += 1
        
print(counts)
```