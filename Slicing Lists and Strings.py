# Python Tutorial: Slicing Lists and Strings
# https://www.youtube.com/watch?v=ajrtAuDg3yw&ab_channel=CoreySchafer

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# pos_i    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# neg_i  -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

# Access array elemets through positive/negative index numbers
print(my_list[5], my_list[-1], my_list[-10])
# Access a range of elements, the second number is NOT INCLUSIVE
print(my_list[0:5], my_list[0:6], my_list[3:8], my_list[-7:-2])
# Mix and match pos/neg indices
print(my_list[1: -2])
# Access range going until the end of array
print(my_list[1:], my_list[5:])
# Access range starting from the start of array
print(my_list[:-1])
# Copy of the list
print(my_list[:])
# Step specifies to access every specified number of elements (default step = 1)
print(my_list[2:-1:2], my_list[2:-1:1])
# Negative step goes backwards from the start index to the end index (doesn't work unless range in coherent)
print(my_list[2: -1: -1], my_list[-1:2:-1], my_list[-2:1:-1], my_list[-2:1:-2])
# Copy of the list in reverse
print(my_list[::-1])

sample_url = 'http://coreyms.com'
print(sample_url)

# Reverse the url
print(sample_url[::-1])
# Get the top level domain
print(sample_url[-4:])
# Get the url without the http://
print(sample_url[7:])
# Get the url without the http:// or the top level domain
print(sample_url[7:-4])