# Chapter 7: Files
## Exercise 1
###  Write a program to read through a file and print the contentsof the file (line by line) all in upper case. Executing the program will look as follows:

```
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
```
```python
fhand = open('exercise-files/mbox-short.txt')
for line in fhand :
    line.upper().rstrip()
    print(line)
```

## Exercise 2
### Write a program to prompt for a file name, and then read through the file and look for lines of the form: `X-DSPAM-Confidence: 0.8475`. When you encounter a line that starts with `X-DSPAM-Confidence:` pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence. values from these lines. When you reach the end of the file, print out the average spam confidence.

```python
fname = input('Enter file path: ')

try :
    fhand = open(fname)
    
except :
    print(f'File {fname}, not found')
    print('Setting path to exercise-files\mbox-short.txt')
    fname = 'exercise-files\mbox-short.txt'
    fhand = open(fname) 
    
count = 0
dsum = 0

for line in fhand :
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    colpos = line.find(':')
    dspam = float(line[colpos + 1:])
    count = count + 1
    dsum = dsum + dspam

print(f'Average spam confidence: {dsum/count}')
```
## Exercise 3
### Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:

```
python egg.py
Enter the file name: mbox.txt
There were 1797 subject lines in mbox.txt
python egg.py
Enter the file name: missing.tyxt
File cannot be opened: missing.tyxt
python egg.py
Enter the file name: na na boo boo
NA NA BOO BOO TO YOU - You have been punk'd!
```
```python
fname = input('Enter file path: ')

try :
    if fname == 'na na boo boo' :
        print("'NA NA BOO BOO TO YOU - You have been punk'd!")
    fhand = open(fname)
    
except :
    print(f'File {fname}, not found')
    print('Setting path to exercise-files\mbox-short.txt')
    fname = 'exercise-files\mbox-short.txt'
    fhand = open(fname) 
    
count = 0
dsum = 0

for line in fhand :
    if not line.startswith('X-DSPAM-Confidence:') :
        continue
    colpos = line.find(':')
    dspam = float(line[colpos + 1:])
    count = count + 1
    dsum = dsum + dspam

print(f'Average spam confidence: {dsum/count}')
```