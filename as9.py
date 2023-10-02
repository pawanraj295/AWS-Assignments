
# 1. Creating an odd sequence from the given sequence [1,2,34,65,1,2,65,66,44,33,22,87,123412,09,78,76]

given_sequence = [1,2,34,65,1,2,65,66,44,33,22,87,123412,9,78,76]
odd_sequence = [num for num in given_sequence if num % 2 != 0]
print(odd_sequence)


# 2. Generating a comprehension of fruits which has more than 20 from the dictionary

fruits = {'apple': 10, 'mango': 20, 'pineapple': 25, 'orange': 30, 'strawberry': 50, 'jackfruit': 10}
fruits_more_than_20 = {fruit: quantity for fruit, quantity in fruits.items() if quantity > 20}
print(fruits_more_than_20)