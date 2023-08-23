# Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements
# https://www.youtube.com/watch?v=DZwmZ8Usvnk&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=6&ab_channel=CoreySchafer

# Example Conditional Statements
if True:
    print('Conditional was True')
if False:
    print('Conditional was True')

# Comparison Operators:
# Equal:                ==
# Not Equal:            !=
# Greater Than:         >
# Less Than:            <
# Greater or Equal:     >=
# Less or Equal:        <=
# Object Identity:      is

# Example if statement using comparisons
language = 'Python'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

# Example if-else statement
language = 'Java'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

# Example if-elif-else statement
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

# Python does not have a swtich-case statement since elif statements suffice

# Combination Boolean statements
user = 'Admin'
logged_in = False

# and keyword
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# or keyword
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# not keyword
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

# is keyword/operator
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
print(a is b)  # False

# id() function to get the memory id of object, which is compared using 'is' keyword
print(id(a))
print(id(b))

b = a
print(id(a))
print(id(b))
print(a is b)
print(id(a) == id(b))

# Boolean evaluation

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example '', (), []
# Any empty mapping. For example {}

# Everything else evaluates to True

conditions = [False, None, 0, 0.0, '', (), [], {}]

for condition in conditions:
    if condition:
        print(f'{str(condition)}, Evaluated to True')
    else:
        print(f'{str(condition)}, Evaluated to False')
