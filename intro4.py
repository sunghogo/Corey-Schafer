# L4: Lists, Tuples, and Sets
# https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4&ab_channel=CoreySchafer

# Declare and create lists
courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))

# Access list values by index
print(courses[3])
# Access last list values by using index -1
print(courses[-1])

try:
    print(courses[4])
except:
    print('No index')

# Index Silcing
# Access index up to but not including second index
print(courses[0:2])
# Start from beginning
print(courses[:2])
# Start at index
print(courses[2:])

# list methods
courses.append('Art')
print(courses)

# Insert at index, value
print(len(courses))
courses.insert(0, 'Art')
print(courses)

# Nested Lists
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses)

# List extensions
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.extend(courses_2)
print(courses)

# Alternative to extension
courses = ['History', 'Math', 'Physics', 'CompSci']
courses += courses_2
print(courses)

# List value removal
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses)

# pop returns the value that was removed
popped = courses.pop()
print(popped)
print(courses)

# List sorting
courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

# sort() defaults to alphabetical descending order
courses.sort()
print(courses)

# sort() defaults to numerical ascending order
nums = [1, 5, 2, 4, 3]
nums.sort()
print(nums)

# sort(reverse=True) to sort alphabetical ascending / numerical descending
courses.sort(reverse=True)
print(courses)
nums.sort(reverse=True)
print(nums)

# Instead of using methods that changes the original lists, use functions
courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)

print(courses)
print(sorted_courses)

# Sequence functions
print(min(nums))
print(max(nums))
print(sum(nums))

# Search for list values and return index
print(courses.index('CompSci'))
try:
    print(courses.index('Art'))
except:
    print("""Traceback (most recent call last):
  File "C:\\Users\\leina\Desktop\\Corey-Schafer\\intro4.py", line 97, in <module>      
    print(courses.index('Art'))
          ^^^^^^^^^^^^^^^^^^^^
ValueError: 'Art' is not in list""")

# Boolean searches
print('Art' in courses)
print('Math' in courses)

# Iteration
for item in courses:
    print(item)
for course in courses:
    print(course)

# Iteration by index; enumerate() outputs two values: index, value
for index, course in enumerate(courses):
    print(index, course)
# Specify start by start=index option
for index, course in enumerate(courses, start=1):
    print(index, course)

# List string casting using "string".join()
course_str = ', '.join(courses)
print(type(course_str), course_str)

course_str = ' - '.join(courses)
print(type(course_str), course_str)

# Split string using .splt() method, and returns values as a list
new_list = course_str.split(' - ')
print(type(new_list), new_list)

# Tuples: Lists are mutable but tuples are immutable
# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# This changes both list_! and list_2 because they are both the same mutable object
list_1[0] = 'Art'

print(list_1)
print(list_2)

# Immutable: Tuples will have less methods due to immutability
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

try:
    tuple_1[0] = 'Art'
except:
    print("""Traceback (most recent call last):
  File "C:\\Users\\leina\\Desktop\\Corey-Schafer\\intro4.py", line 155, in <module>     
    tuple_1[0] = 'Art'
    ~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment""")

print(tuple_1)
print(tuple_2)

# Sets are values that are not ordered and haven o duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

# Sets will appear in different orders
print(cs_courses)

# Duplicate values will be removed
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)

# Membershp tests are more efficient that lists and tuples
print('Math' in cs_courses)

# Determine which values multiple sets share and don't share more efficiently
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

# .intersection() and . difference() methods
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))

# .union() method to see all values
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = {}
empty_tuple = tuple()

# Empty Sets
# empty+set = {} # This isn't right! This creates an empty dictionary
empty_set = set()
