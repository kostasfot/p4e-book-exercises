# Chapter 4: Functions
## Exercise 1
### Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.
```python
import random
for i in range(10):
    x = random.random()
    print(x)
```

## Exercise 2
### Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.
```python
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
    
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()
```
```
NameError: name 'repeat_lyrics' is not defined
```
## Exercise 3
### Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics. What happens when you run this program?
The program runs correctly

## Exercise 4
### What is the purpose of the “def” keyword in Python?
a) It is slang that means “the following code is really cool”  
*b) It indicates the start of a function*  
c) It indicates that the following indented section of code is to be stored for later  
d) b and c are both true  
e) None of the above

## Exercise 5
### What will the following Python program print out?
```python
def fred():
    print("Zap")
def jane():
    print("ABC")
    
jane()
fred()
jane()
```
a) Zap ABC jane fred jane  
b) Zap ABC Zap  
c) ABC Zap jane  
*d) ABC Zap ABC*  
e) Zap Zap Zap

## Exercise 6
### Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
```python
def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)

        pay = hours * rate

        if hours > 40 :
            pay = ((rate * 0.5) * (hours - 40)) + pay
        
    except:
        print('Error, enter a numeric input')

    return pay

computepay(45, 10)
```

## Exercise 7
### Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
```python
def computegrade(score) :

    grade = str()

    try :
        score = float(score)
    except :
        grade = 'Bad score'
    
    if score < 0 or score > 1 :
        grade = 'Bad Score'
    elif score < 0.6 :
        grade = 'F'
    elif score > 0.6 and score <= 0.7 :
        grade = 'D'
    elif score > 0.7 and score <= 0.8 :
        grade = 'C'
    elif score > 0.8 and score <= 0.9 :
        grade = 'B'
    elif score > 0.9 :
        grade = 'A'
    
    return grade
```