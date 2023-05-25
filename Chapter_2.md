# Chapter 2: Variables, expressions, and statements
## Exercise 1
### Type the following statements in the Python interpreter to see what they do:
```python
5
x = 5
x + 1
```
1. Type `5` and press Enter:  
Output: `5` 
Explanation: The number 5 is evaluated and displayed as the result.
2. Type `x = 5` and press Enter:  
Output: No output (the assignment is stored in memory)  
Explanation: The variable `x` is assigned the value of `5`.
3. Type `x + 1` and press Enter:  
Output: 6  
Explanation: The expression `x + 1` is evaluated, where `x` is the variable with a value of `5`. The result, `6`, is displayed.

## Exercise 2
### Write a program that uses input to prompt a user for their name and then welcomes them.
```python
name = input('Enter your name:\n')
print('Hello', name)
```

## Exercise 3
### Write a program to prompt the user for hours and rate per hour to compute gross pay.
```python
hours = input('Enter Hours:\n')
rate = input('Enter Rate:\n')

hours = float(hours)
rate = float(rate)

pay = hours * rate
print('Pay:', pay)
```

## Exercise 4 Assume that we execute the following assignment statements:
```python
width = 17
height = 12.0
```
For each of the following expressions, write the value of the expression and the type (of the value of the expression).
1. `width//2` -> 8
2. `width/2.0` -> 8.5
3. `height/3` -> 4.0
4. `1 + 2 * 5` -> 11

## Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
```python
cel = float(input('Provide the temperature in Celsius:\n')) # Prompt the user to provide temperature in celsius
fahr = (cel * 9/5) + 32 # Fahrenheit converion

print('The temperature in Fahrenheit is:', fahr)
```
