# Python Tutorial for Beginners 4: Lists, Tuples, and Sets
# https://www.youtube.com/watch?v=W8KRzm-HUcc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=4&ab_channel=CoreySchafer

# Declare dictionary and key-value pairs
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name'], student['age'], student['courses'])

# Keys and values can be any data type
student[1] = '1'
print(student[1])

# Accessing nonexistent keys throws an error, use dictionary .get method
try:
    print(student['phone'])
except Exception as e:
    print(type(e))

print(student.get('name'))

# Returns None if key doesn't exist, or specified default value
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

# Adding new entries to dictionary
student['phone'] = '555-5555'
print(student.get('phone', 'Not Found'))

# Updating entries
student['name'] = 'Jane'
print(student)

# Updating multiple entries at a time using .update dictionary method
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)

# Deleting entries using del keyword and .pop method
del student['name']
age = student.pop('age')
print(age)
print(student)

# Find number of entries in dictionary
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(len(student))

# Find all keys in dictionary using .keys method
print(student.keys())

# Find all values in dictionary using .values method
print(student.values())

# Find all key-value pairs in dictionary using .items method
print(student.items())

# Iterating through entries in dictionary
# Iterate through keys
for key in student:
    print(key)
for key in student.keys():
    print(key)

# Iterate through values
for value in student.values():
    print(value)

# Iterate through key-value pairs
for key, value in student.items():
    print(key, value)
