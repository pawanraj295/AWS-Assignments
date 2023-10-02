Name = "Rammohan"

# Convert the string to uppercase
upper_name = Name.upper()
print(upper_name)

# Convert the string to lowercase
lower_name = Name.lower()
print(lower_name)

# Convert the first character of the string to uppercase
capitalized_name = Name.capitalize()
print(capitalized_name)

# Replace 'e' with 'E'
replaced_name = Name.replace('e', 'E')
print(replaced_name)

L = [1, 2, 3]

# Extend the list
L.extend([5, 6, 7])
print(L)

# Remove the fifth value
del L[4]
print(L)

d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

# Remove out-of-stock fruits
d = {fruit:quantity for fruit, quantity in d.items() if quantity > 0}
print(d)

# Update mango quantity to 15
d['mango'] = 15

# Decrease pineapple quantity by 5
d['pineapple'] -= 5

print(d)

