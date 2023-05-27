# Chapter 8: Lists
## Exercise 1
### Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

```python
def chop(t) :
    del t[0]
    del t[-1]

def middle(t) :
    return t[1:-1]
```

## Exercise 2
### Figure out which line of the above program is still not properly guarded. See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

```python
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
```

The line that is not properly guarded in the given program is the line print words[2]. It assumes that there will always be at least three words in a line before accessing words[2]. However, if there is a line with fewer than three words, it will cause an "IndexError" and the program will fail.

To guard against this issue, we can add a check before accessing words[2] to ensure that the list words contains at least three elements. Here's the modified program:

```python
fhand = open('exercise-files/mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) < 3:  # Guard against lines with fewer than three words
        continue
    if len(words) == 0:  # Skip empty lines
        continue
    if words[0] != 'From':  # Skip lines that don't start with 'From'
        continue
    print(words[2])
```

## Exercise 3
### Rewrite the guardian code in the above example without two if statements. Instead, use a compound logical expression using the or logical operator with a single if statement.

```python
fhand = open('exercise-files/mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    if len(words) == 0 or len(words) < 3:  # One logical statement
        continue
    if words[0] != 'From':  # Skip lines that don't start with 'From'
        continue
    print(words[2])
```

## Exercise 4
###  Find all unique words in a file Shakespeare used over 20,000 words in his works. But how would you determine that? How would you produce the list of all the words that Shakespeare used? Would you download all his work, read it and track all unique words by hand? Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work. To get started, download a copy of the file www.py4e.com/code3/romeo.txt. Create a list of unique words, which will contain the final result. Write a program to open the file romeo.txt and read it line by line. For eachline, split the line into a list of words using the split function. For each word, check to see if the word is already in the list of unique words. If the word is not in the list of unique words, add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

```
Enter file: romeo.txt
['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
'and', 'breaks', 'east', 'envious', 'fair', 'grief',
'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
'sun', 'the', 'through', 'what', 'window',
'with', 'yonder']
```

```python
fhand = open('exercise-files/romeo.txt')
unique = list()
for line in fhand :
    words = line.split()
    for word in words :
        if word not in unique :
            unique.append(word)

unique.sort()
print(unique)
```

## Exercise 5
### Minimalist Email Client.
### MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by early email servers and desktop apps. Without getting into too many details, MBOX is a text file, which stores emails consecutively. Emails are separated by a special line which starts with From (notice the space). Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails. Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. We are interested in who sent the message, which is the second word on the From line.  
### `From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008`
### You will parse the From line and print out the second word for each From line, then you will also count the number of From (not From:) lines and print out a count at the end. This is a good sample output with a few lines removed:

```
python fromcount.py
Enter a file name: mbox-short.txt
stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
[...some output removed...]
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
```
```python
fhand = open('exercise-files/mbox-short.txt')
count = 0
for line in fhand :
    if not line.startswith('From ') :
        continue
    words = line.split()
    print(words[1])
    count = count + 1
print(f'There were {count} lines in the file with From as the first word')
```