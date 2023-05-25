# Chapter 1: Why you should learn to program.
## Exercise 1
### What is the function of the secondary memory in a computer?
a) Execute all of the computation and logic of the program  
b) Retrieve web pages over the Internet  
*c) Store information for the long term, even beyond a power cycle*  
d) Take input from the user  

## Exercise 2
### What is a program?
A set of instructions that specifies a computation.

## Exercise 3
### What is the difference between a compiler and an interpreter?
**Compiler**: Translates the whole code first, then runs it.  
**Interpreter**: Translates and runs the code line by line.  
A compiler does the translation work upfront and creates a standalone program, while an interpreter does the translation and execution together, line by line, as the program runs.  

## Exercise 4
### Which of the following contains “machine code”?
*a) The Python interpreter*  
b) The keyboard  
c) Python source file  
d) A word processing document  

## Exercise 5
### What is wrong with the following code:
```python
>>> primt 'Hello world!'
File "<stdin>", line 1
primt 'Hello world!'
^
SyntaxError: invalid syntax
>>>
```
The error in the code is a typo in the function name. Instead of using the correct function name "print", it is written as "primt". As a result, the code encounters a SyntaxError indicating "invalid syntax" because the interpreter does not recognize the misspelled function name. To fix the code, the correct spelling of the function should be used. Here's the corrected code:
```python
print('Hello world!')
```

## Exercise 6
### Where in the computer is a variable such as “x” stored afterthe following Python line finishes?
`x = 123`
a) Central processing unit  
*b) Main Memory*  
c) Secondary Memory  
d) Input Devices  
e) Output Devices  

## Exercise 7
### What will the following program print out:
```python
x = 43
x = x - 1
print(x)
```
The given program will print out: `42`. Here's a breakdown of what happens in the program:  
1. The variable x is assigned the initial value of 43.
2. The line x = x - 1 subtracts 1 from the current value of x (which is 43) and assigns the result (42) back to x.
3. Finally, the line print(x) outputs the value of x, which is now 42.

## Exercise 8
### Explain each of the following using an example of a human capability: (1) Central processing unit, (2) Main Memory, (3) Secondary Memory, (4) Input Device, and (5) Output Device. For example, “What is the human equivalent to a Central Processing Unit”?
1. Central Processing Unit (CPU): The human equivalent to a CPU is the brain. Like the brain, the CPU processes instructions and performs calculations, serving as the computer's control center.
2. Main Memory: Main Memory is comparable to our short-term memory. It stores data and instructions temporarily for quick access during tasks, much like how our short-term memory holds information temporarily.
3. Secondary Memory: Secondary Memory, like our long-term memory, provides non-volatile storage for data that persists even when the computer is powered off, similar to how our long-term memory retains information over extended periods.
4. Input Device: Input devices, such as keyboards or microphones, are akin to our sensory organs. They allow the computer to receive external information, like how our senses provide input to our brain for processing.
5. Output Device: Output devices, like monitors or speakers, act as our means of communication and expression. They present processed information or enable the computer to communicate results, similar to how we communicate our thoughts through speech or writing.

## Exercise 9
### How do you fix a “Syntax Error”?
To fix a "Syntax Error," carefully read the error message to identify the line and nature of the error. Review the code near the error, checking for typos, missing/extra characters, matching pairs, correct keyword usage, proper indentation, and valid symbols. Make necessary corrections based on language rules.




