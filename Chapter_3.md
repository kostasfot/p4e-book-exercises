# Chapter 3: Conditional Execution
## Exercise 1
### Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
```python
rate = float(input('Enter Rate:\n'))
hours = float(input('Enter Hours:\n'))

pay = rate * hours

if hours > 40 :
    pay = (hours - 40) * (rate * 0.5) + pay

print('Pay:', pay)
```

## Exercise 2
### Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
```
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
```
```python
try:
    hours = float(input('Enter Hours:\n'))
    rate = float(input('Enter rate:\n'))
    
    pay = rate * hours

    if hours > 40 :
        pay = (hours - 40) * (rate * 0.5) + pay

    print('Pay:', pay)
except:
    print('Error, please enter numeric input')
```

## Exercise 3
### Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
```
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
Enter score: 0.95
A
Enter score: perfect
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
F
```
```python
try:
    score = float(input('Enter score:\n'))

    if score > 1 or score < 0 :
        print('Bad score')
    elif score < 0.6 :
        print('F')
    elif score >= 0.6 and score < 0.7 :
        print('D')
    elif score >= 0.7 and score < 0.8 :
        print('C')
    elif score >= 0.8 and score < 0.9:
        print('B')
    elif score >= 0.9 :
        print('A')
except:
    print('Bad score')
```
