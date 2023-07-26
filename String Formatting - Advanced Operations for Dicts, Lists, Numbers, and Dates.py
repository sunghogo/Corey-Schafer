# Python Tutorial: String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates
# https://www.youtube.com/watch?v=vTX3IwquFkc&ab_channel=CoreySchafer

person = {'name': 'Jenn', 'age': 23}

# Basic string concatenation that is not readable
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

# Using string formatting option
sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
print(sentence)
# Passing in the numbers to specify argument in formatting option
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)

# String formatting option with repeated values
tag = 'hi'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

# Accessing dictionary values in string formatting
l = ['Jenn', 23]
sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
print(sentence)
sentence = 'My name is {0[0]} and I am {1[1]} years old.'.format(l, l)
print(sentence)

# Accessing attributes values in string formatting
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {1.age} years old.'.format(p1, p1)
print(sentence)

# String formatting option using keyword arguments
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
print(sentence)

# Unpacking dictionry for string formatting option keyword arguments
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)

print(*person)
# print(**person)

# Format numbers using string formatting
for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)
    
    # Pad numbers with 0 up to 3 digits
    sentence = 'The value is {:03}'.format(i)
    print(sentence)

# Formatting decimal numbers using string formatting option
import math
pi = math.pi

sentence = 'Pi is equal to {}'.format(pi)
print(sentence)

# Specify to 3 decimal places
sentence = 'Pi is equal to {:.3f}'.format(pi)
print(sentence)

# Print out large numbers with comma separators
sentence = '1 MB is equal to {:,} bytes'.format(1024**2)
print(sentence)

# Combine both comma separators and specify decimal places
sentence = '1 MB is equal to {:,.2f} bytes'.format(1024**2)
print(sentence)

# Format datetime
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

# Format in Month Day, Year
sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

# Format in Month Day, Year fell on a Weekday and was the NUM day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)