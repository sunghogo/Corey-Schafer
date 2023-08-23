# Python Tutorial for Beginners 3: Integers and Floats - Working with Numeric Data
# https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=3&ab_channel=CoreySchafer

# type() function gives data type of variable/value
num = 3
print(type(num))

num = 3.14
print(type(num))

# Artihmetic Operators:
# Addition:
print(3 + 2)
# Subtraction:
print(3 - 2)
# Multiplication:
print(3 * 2)
# Division:
print(3 / 2)
# Floor Division:
print(3 // 2)
# Exponent:
print(3 ** 2)
# Modulus:
print(3 % 2)

# Order of Operations with parentheses
print(3 * 2 + 1)
print(3 * (2 + 1))

# Incrementing variables
num = 1
num = num + 1
print(num)

num += 1
print(num)

num *= 1
print(num)

# Built-in function
print(abs(-3))
print(round(3.75))
print(round(3.75, 1))

# Comparison Operators:
# Equal:
print(3 == 2)
# Not Equal:
print(3 != 2)
# Greater Than:
print(3 > 2)
# Less Than:
print(3 < 2)
# Greater or Equal
print(3 >= 2)
# Less or Equal:
print(3 <= 2)

# String and number casting
num_1 = '100'
num_2 = '200'
print(num_1 + num_2)

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)
