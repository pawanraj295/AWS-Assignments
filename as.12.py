#my_module.py

def is_palindrome(word):
    # Check if the word is a palindrome
    return word == word[::-1]

def fibonacci(n):
    # Generate n Fibonacci numbers
    fib_seq = []
    a, b = 0, 1
    while len(fib_seq) < n:
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq

def factorial(n):
    # Calculate the factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)