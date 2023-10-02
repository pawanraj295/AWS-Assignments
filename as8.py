#Replicating the built-in sum() function: 
def custom_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
nums = [1, 2, 3, 4, 5]
result = custom_sum(nums)
print(result) 

#Replicating ljust() and rjust() string methods: 
def custom_ljust(string, width, fillchar=' '):
    if len(string) >= width:
        return string
    else:
        padding_length = width - len(string)
        padding = fillchar * padding_length
        return string + padding

def custom_rjust(string, width, fillchar=' '):
    if len(string) >= width:
        return string
    else:
        padding_length = width - len(string)
        padding = fillchar * padding_length
        return padding + string

text = "Hello"
width = 10
result1 = custom_ljust(text, width, fillchar='_')
result2 = custom_rjust(text, width, fillchar='_')
print(result1) 
print(result2)   

#Functions for Palindrome, Fibonacci, and Factorial:

# Palindrome function
def is_palindrome(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    return num_str == reversed_str

# Fibonacci function
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

# Factorial function
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = 12321
is_palindrome_result = is_palindrome(num)
print(is_palindrome_result)  

fibonacci_sequence = fibonacci(10)
print(fibonacci_sequence) 

factorial_result = factorial(5)
print(factorial_result)


#Generating a range of numbers:  
def generate_number_range(start, end, step=1):
    return list(range(start, end, step))

# Example usage
start = 1
end = 10
step = 2
result = generate_number_range(start, end, step)
print(result) 

