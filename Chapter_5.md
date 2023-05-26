# Chapter 5: Iteration
## Exercise 1
### Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

```python
total = 0
count = 0

while True :
    num = input('Enter a number:')
    
    if num == 'done' :
        break
    try :
        num = float(num)
    except :
        print('Enter numeric input')
        continue
    
    total = total + num
    count = count + 1
    
print('Total:', total)
print('Count:', count)
print('Average:', total / count)
```

## Exercise 2
### Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

```python
total = 0
count = 0
mnm = None
mxm = None

while True :
    num = input('Enter a number:')
    
    if num == 'done' :
        break
    try :
        num = float(num)
    except :
        print('Enter numeric input')
        continue
    
    if mnm == None or num < mnm :
        mnm = num
    
    if mxm == None or num > mxm :
        mxm = num
    
    total = total + num
    count = count + 1
    
print('Total:', total)
print('Count:', count)
print('Minimum:', mnm)
print('Maximum:', mxm)
```