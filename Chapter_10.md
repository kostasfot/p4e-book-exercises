# Chapter 9: Dictionaries
## Exercise 1
### Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

### After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

```python
mails = dict()
lst = list()

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File cannot be opened:', fname)
    fhand = open('exercise-files/mbox-short.txt')

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue
    else:
        if words[1] not in mails:
            mails[words[1]] = 1
        else:
            mails[words[1]] += 1

for key, val in list(mails.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for count, email in lst[:1]:
    print(email, count)
```
```
Sample Line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
```

## Exercise 2
### This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

```python
fname = input('Enter file path')
hours = dict()
lst = list()

try:
    fhand = open(fname)
except:
    print('FIle not found, Setting mbox.txt')
    fhand = open('exercise-files/mbox-short.txt')


for line in fhand:
    words = line.split()
    if len(words) < 5 or words[0] != 'From': 
        continue
    
    colpos = words[5].find(':')
    hour = words[5][:colpos]
    if hour not in hours:
        hours[hour] = 1
    else:
        hours[hour] += 1

for key, val in list(hours.items()):
    lst.append((key, val))
    
lst.sort()

for key,val in lst:
    print(key,val)
```

## Exercise 3
### Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies

```python
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
```