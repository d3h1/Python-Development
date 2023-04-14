# ----------------------------------------------
# Variables are dynamically typed -- type determined at runtime
print('\n----------------------------------------------')
print('VARIABLES')
print('----------------------------------------------')

n = 0
print(f'n is: {n}')

n = 'abc'
print(f'n is now: {n}')

# Multiple Assignments
n, m = 0, 'abc'
n, m, z = 0.1, 'abc', False

# Increment
n = n + 1 # good
n += 1 # good
# n++ # bad

'''NONE IS NULL (absence of value) -- 
can assign to value and then null
'''
n = 4
n = None
# ----------------------------------------------

# ----------------------------------------------
# IF / ELSE does not need () usually, always :
print('\n----------------------------------------------')
print('IF ELSE -- see code')
print('----------------------------------------------')

n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 4 

# Parentheses needed for multi line conditionals
# and : &
# or : ||
n, m = 1, 2
if ((n > 2 and 
    n != m) or 
    n == m):
    print('success')
    n += 1
# ----------------------------------------------

# ----------------------------------------------

# WHILE LOOPS are similar
print('\n----------------------------------------------')
print('LOOPS')
print('----------------------------------------------')

m = 0
while m < 5:
    print(m)
    m += 1

# FOR LOOPS
# Looping from i=0 to i=4
for i in range(5):
    print(i, ',')

# Looping from i=2 to i=5
for i in range(2, 6):
    print(i)

# Looping from i=5 to i=2 -- pass through a -1 to show decrementing
for i in range(5, 1, -1):
    print(i)

# ----------------------------------------------

# ----------------------------------------------
# Division is decimal by default -- decimal division
print('\n----------------------------------------------')
print('DIVISION')
print('----------------------------------------------')

print(5 / 2)

# Double slash rounds down -- integer division
print(5 // 2)

# CAREFUL: most langs round towards 0 by default
# This means that negative number round down
print(-3 // 2) # prints -2 instead of -1

# WORKAROUND divide and make it an int so that it
# will round towards zero through decimal division
print(int(-3 / 2)) # prints -1 instead of -2

# Modding is similar to most languages
print(10 % 3) # Remainder is 1

# Different with negative values 
print(-10 % 3)

# To be consistent with other langs modulo -- import math
import math
print(math.fmod(-10, 3))

# MATH HELPERS
print(math.floor(3 / 2)) # Round down
print(math.ceil(3 / 2)) # Round up
print(math.sqrt(49)) # Square Root
print(math.pow(2, 3)) # 2 ^ 3

# Max Int | Min Int
float('inf')
float('-inf')

# Python numbers are infinite so they never overflow 
# This means that even large numbers are still less than infinity
print((math.pow(2, 200)) < float('inf'))
# ----------------------------------------------

# ----------------------------------------------
# ARRAYS -- LISTS -> They are dynamic
print('\n----------------------------------------------')
print('ARRAYS')
print('----------------------------------------------')

arr = [1, 2, 3]
print(arr)

# Can be used as a stack -- because not actually stack, 
# WE can still do things like insert 

# APPEND 0(1)
arr.append(4) # Adds 4 to array
arr.append(5) # Adds 5 to array
print(arr)
# POP 0(1)
arr.pop() # Removes last number from arr
print(arr)
# INSERT 0(n)
arr.insert(1, 7) # Inserts 7 on index 1 (whatever idx we want)
print(arr) 
# REINDEX 0(1)
arr[0] = 0
arr[3] = 0
print(arr)

# We can initialize the arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# CAREFUL WHEN INDEXING ARRAY
# -1 is not out of bound but rather the last value
arr = [1, 2, 4]
print(arr[-1])

# -2 is second to last value, etc.
print(arr[-2])

# SUB-LISTS (SLICING)
arr = [1, 2, 3, 4]
# from index 1, 2, 3 but not including 
# index 3 just like for loops as last index
# is non inclusive
print(arr[1:3])
print(arr[0:4])

# UNPACKING
a, b, c = [1, 2, 3] # Both sides to need to match amount 
# Take all individual parts of array and reassign them
# CAN BE SUPER USEFUL when you want to go through 
# a list of pairs

# LOOP THROUGH ARRAYS
nums = [1, 2, 3]


# Using index -- if you need index and value like two sum
for i in range(len(nums)):
    print(nums[i])

# Without using index 
for n in nums:
    print(n)

# ENUMERATE
# Rather, with index and value
for i, n in enumerate(nums):
    print(i, n)

# LOOP THROUGH MULTIPLE ARRAYS at the same time
# with UNPACKING
nums1 = [1, 2, 3]
nums2 = [4, 24, 31]
for n1, n2 in zip(nums1, nums2): # Combines both
    print (n1, n2)
# ----------------------------------------------
    
# ----------------------------------------------
# REVERSING AN ARRAY
print('\n----------------------------------------------')
print('ARRAY FUNCTIONS')
print('----------------------------------------------')

nums = [1, 2, 3]
nums.reverse()
print(nums)

# SORTING AN ARRAY in ascending
arr = [5, 10, 9, 1, 2, 6]
arr.sort()
print(arr)

# SORTING AN ARRAY in descending
arr.sort(reverse=True)
print(arr)

# SORTING AN ARRAY by alphabetical
names = ['bob', 'alice', 'jane', 'doe']
names.sort()
print(names)

# CUSTOM SORT by length
names.sort(key = lambda x: len(x)) # Lambda is function without name
print(names)

# LIST COMPREHENSION
arr = [i for i in range(5)]
print(arr)
arr = [i+i for i in range(5)]
print(arr)

# 2-D ARRAYS
# ie we want to make 4 unique rows -- how do we 
arr = [[0] * 4 for i in range(4)]
print(arr)

# this below doesn't work because then each is not unique
arr = [[0] * 4] * 4
print(arr)
# ----------------------------------------------

# ----------------------------------------------
# STRINGS -- THEY ARE IMMUTABLE
print('\n----------------------------------------------')
print('STRINGS')
print('----------------------------------------------')

s = 'abc'
print(s[0:3])
# So you cannot change the value of an index in a string unlike arrays
# s[0] = 'A' # Will throw a type error 

# You can UPDATE string but it creates a new rather
s += 'def'
print(s)

# Strings can be converted into integers and vice versa
s = '123'
print(type(int(s))) 
print(type(str(123)))

# You can even get ASCII chars with ORD
print(ord('a'))

# COMBINE STRING WITH DELIMITER (empty or etc...)
letters = ['ab', 'cd', 'ef']
print(''.join(letters))
print(','.join(letters)) # Anything you want
# ----------------------------------------------

# ----------------------------------------------
# QUEUES (double ended queue) FIRST IN FIRST OUT FIFO 0(1)
# all can be done in constant time unlike stack
print('\n----------------------------------------------')
print('QUEUES')
print('----------------------------------------------')

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop() # Can be done to the right also
print(queue)
# ----------------------------------------------

# ----------------------------------------------
# HASHSETS 0(1) -- We can search, insert, remove into them in constant time
# NO DUPLICATES
print('\n----------------------------------------------')
print('HASHSETS')
print('----------------------------------------------')

mySet = set()
mySet.add(1)
mySet.add(2)

print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

mySet = set()
mySet.add('a')
print(mySet)

# LIST TO SET
arr = [1, 2, 3] # List
print(arr) 
print(set(arr)) # List -> Set

# SET COMPREHENSION -- looping to create a whole set
mySet = { i for i in range(5) }
print(mySet)
# ----------------------------------------------

# ----------------------------------------------
# HASHMAPS (AKA DICTIONARIES)
print('\n----------------------------------------------')
print('HASHMAPS')
print('----------------------------------------------')
myMap = {}
myMap['alice'] = 88
print(myMap)

