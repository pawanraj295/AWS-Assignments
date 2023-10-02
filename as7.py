#upper() and .lower() Functions using capitalize() Function

s = "Hello World!"

# Replicating .upper() method
s_upper = s.capitalize().replace(s[0], s[0].upper())
print(s_upper)    # "HELLO WORLD!"

# Replicating .lower() method
s_lower = s.capitalize().replace(s[0], s[0].lower())
print(s_lower)    # "hello world!" 

#Generating an Odd Sequence from an Existing List:
seq = [1,2,34,65,1,2,65,66,44,33,22,87,123412,9,78,76]

odd_seq = [x for x in seq if x % 2 != 0]
print(odd_seq) 

#Dictionary Comprehension to Filter Fruits with More than 20:
fruits = {'apple': 10, 'mango': 20, 'pineapple': 25, 'orange': 30, 'strawberry': 50, 'jackfruit': 10}

fruits_more_than_20 = {key: value for key, value in fruits.items() if value > 20}
print(fruits_more_than_20) 