# Python Tutorial for Beginners 7: Loops and Iterations - For/While Loops
# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=7&ab_channel=CoreySchafer

# Quick recap of looping through list
nums = [1, 2, 3, 4, 5]

# for loops
for num in nums:
    print(num)

# break keyword to stop iteration
for num in nums:
    if num == 3:
        print('Found 3!')
        break
    print(num)

# continue keyword to shortcircuit to next iteration
for num in nums:
    if num == 3:
        print('Found 3!')
        continue
    print(num)

# nested loops, may be time consuming
for num in nums:
    for letter in 'abc':
        print(num, letter)

# looping using a range
for i in range(10):
    print(i)  # prints 0 to 9

# Specify range
for i in range(1, 11):
    print(i)  # prints 1 to 10

# while loops continue until certain condition is met/a break
x = 0
while x < 10:
    print(x)
    x += 1

# infinite while loop using break
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1

# Using CTRL + C to cancel program if stuck in infinite loop
