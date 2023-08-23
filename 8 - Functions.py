# Python Tutorial for Beginners 8: Functions
# https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=8&ab_channel=CoreySchafer

# Functions are instructions packaged together to perform a specific task
# def keyword to declare a function
# pass keyword to leave a statement blank
def hello_func():
    print('Hello Function!')
    return 'Hello Function.'


# Print function location in memory
print(hello_func)

# Call functions
hello_func()

# DRY Principle for code management and reusability
print('Hello Function!')
print('Hello Function!')
hello_func()
hello_func()

# Function return values
print(hello_func().upper())


# Pass parameters/arguments to function
def hello_func_2(greeting):
    return f'{greeting} Function.'


# Functions with positional parameters require the positional argument to be passed
try:
    hello_func_2()
except Exception as e:
    print(type(e))

print(hello_func_2('Hi'))


# Functions can have keyword parameters with default values to do not need to be passed
def hello_func_3(greeting, name='You'):
    return f'{greeting}, {name}'


print(hello_func_3('Hi'))
print(hello_func_3('Hi', name='Corey'))


# *args specify any number of positional arguments, and **kwargs specify any number of keyword arguments
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# args is a tuple with all our positional arguments, and kargs is a dictionary with all our keyword arguments
student_info('Math', 'Art', name='John', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

# We can pass list and dictionary as our *args and **kargs, but they need to be unpacked first using * and **
student_info(*courses, **info)

# Destructuring lists, no simple way to destructure dictionaries
[arg1, arg2] = courses
print(arg1, arg2)

# Code from std library repurposed for this exercise
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years. False for non-leap years"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2017))
print(is_leap(2020))

print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
