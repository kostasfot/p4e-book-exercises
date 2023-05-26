# Chapter 6: Strings
## Exercise 1
### Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

```python
fruit = 'banana'
index = len(fruit)

while index > 0:
    letter = fruit[index - 1]
    print(letter)
    index = index - 1
```

## Exercise 2
### Given that fruit is a string, what does `fruit[:]` mean?

Given that `fruit` is a variable of type `string` then `fruit[:]` means that we select the whole string, from the first index until the last one.

## Exercise 3
### Encapsulate this code in a function named `count`, and generalize it so tha it accepts the string and the letter as arguments.

```python
word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
        count = count + 1
print(count)
```
```python
def count(word, letter) :
    cnt = 0
    for l in word :
        if l == letter :
            cnt = cnt + 1
    return cnt
```

## Exercise 4
### There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at: [this link](https://docs.python.org/3/library/stdtypes.html#string-methods). Write an invocation that counts the number of times the letter a occurs in “banana”.

```python
'banana'.count('a')
```

## Exercise 5
### Take the following python code that stores a string: `str = -DSPAM-Confidence:0.8475'` Use find and string slicing to extract the portion of the string after the colon character and the use the `float` function to convert the extracted string into a floating point number.

```python
str = 'DSPAM-Confidence:0.8475'

colpos = str.find(':')
conf = float(str[colpos + 1:])
conf
```