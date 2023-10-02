#Create a Generator function to replicate range(): 
def my_range(start, stop, step=1):
    current = start
    while current < stop if step > 0 else current > stop:
        yield current
        current += step

for i in my_range(1, 10, 2):
    print(i) 
#Create a Recursive function to replicate range(): 

def recursive_range(start, stop, step=1):
    if (step > 0 and start >= stop) or (step < 0 and start <= stop):
        return []
    else:
        return [start] + recursive_range(start + step, stop, step)

print(recursive_range(1, 10, 2))
#Create a Recursive and lambda function - Greatest Common Divisor (GCD):  
gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

print(gcd(48, 18))


 
