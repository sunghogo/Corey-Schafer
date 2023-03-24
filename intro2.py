# L2: Strings - Working with Textual Data
# https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2&ab_channel=CoreySchafer

from string import Template

# Use Descriptive Variable Names
# You can escape characters to use special characters in strings
message = 'Bobby\'s World'
# Use 3 quotes at the beginning and end of string to create multi line strings
message = """Bobby's World was a good
cartoon in the 1990s"""

message = 'Hello World'

print(message)

# len() function to print out length of string
print(len(message))

# Can access acharacters by index position
print(message[10])

# Prints out range up to but not including sexond index
# You can also slice strings
print(message[0:5])
print(message[:5])
print(message[6:])

# Methods are functions that belong to an object
print(message.lower())
print(message.upper())

# Find the count of searched keywords
print(message.count('Hello'))
print(message.count('l'))

# Find the posiion/starting index of searched keyword, or returns -1
print(message.find('World'))
print(message.find('Universe'))

# Methods returns a new value, not executing in place
message = 'Hello World'
new_message = message.replace('World', 'Universe')
print(message)
print(new_message)

# String Concatenation
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome!'
print(message)

# Instead use string formatting
message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

# 3.6+ have f-strings that you can use veriable names directly inside brackets, and works with method calls
i = 5
message = f'{greeting}, {name.upper()}. Welcome! High {i}!'
print(message)

# Template from the standard string library are an alternative way
message = 'Hey $name, there is a $error error!'
temp = Template(message).substitute(name=name, error=hex(i))
print(temp)

# Function to show all the attribute and methods available with that variable
print(dir(name))

# Function for more information on class methods
print(help(str))
print(help(str.lower))
