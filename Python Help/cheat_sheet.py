print('\n----------------------------------------------')
print('VARIABLES dynamically typed -- type determined at runtime')
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

print('\n----------------------------------------------')
print('IF ELSE -- does not need () usually, always :')
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

print('\n----------------------------------------------')
print('DIVISION decimal by default -- decimal division')
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

print('\n----------------------------------------------')
print('ARRAYS - LISTS -> They are dynamic')
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

print('\n----------------------------------------------')
print('STRINGS -- THEY ARE IMMUTABLE')
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

print('\n----------------------------------------------')
print('QUEUES (double ended queue) FIRST IN FIRST OUT FIFO 0(1)')
print('----------------------------------------------')
# all can be done in constant time unlike stack
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

print('\n----------------------------------------------')
print('HASHSETS 0(1) -- We can search, insert, remove into them in constant')
print('----------------------------------------------')
# NO DUPLICATES
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

print('\n----------------------------------------------')
print('HASHMAPS (AKA DICTIONARIES) -- cannot have duplicate keys or values')
print('----------------------------------------------')
myMap = {}
myMap['alice'] = 88
myMap['bob'] = 99
print(myMap)
print(len(myMap))
# WE can change the values of the keys 
# by mapping new values

myMap['alice'] = 90
print(myMap['alice'])
print('alice' in myMap)

# You can also remove keys from a hashmap
myMap.pop('alice')
print('alice' in myMap)

# You can also init a hashmap key:value
myMap = {'alice':40, 'brenda':60}
print(myMap)

# CAN USE DICT COMPREHENSION ALSO
myMap = { i: 2*i for i in range(3)}
print(myMap)

# Loop through maps
print('-----------HASHMAP LOOPS-----------')
myMap = {'alice': 40, 'bob': 50}
for i in myMap:
    print(i, myMap[i])

# You can loop using values keyword
for val in myMap.values():
    print(val)

# Key and Value using items in the map
for key, value in myMap.items():
    print(key, value)


print('\n----------------------------------------------')
print('TUPLES -- Mainly used in Hashsets | Hashmaps')
print('----------------------------------------------')  
# TUPLES -- Like arrays but immutable
tup = (1, 2, 3)    # WE can index but cannot modify unlike arrays
print(tup)
print(tup[0])
print(tup[1])

# CANNOT MODIFY
# tup[0] = 0 -- This will set a type error 

# Can be used in hashmaps and such
myMap = {(1, 2): 3}
print(myMap[(1, 2)])

mySet = set()
mySet.add((1, 2))
print((1, 2) in mySet)

# Lists CANNOT be keys while tuples can
# myMap = [[3, 4]] = 5 This will put out a type error 

print('\n----------------------------------------------')
print('HEAPS -- Find Min and Max of a set of values frequently')
print('----------------------------------------------') 
# BY DEFAULT HEAPS ARE MIN HEAPS
import heapq

# under the hood heaps are implemented by arrays 
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# SINCE NO MAX HEAPS BY DEFAULT -- work around is to 
# use min heap and then multiply by -1 when pushing and popping 
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max will always be at zero but this time you have to multiply by -1
print(-1 * maxHeap[0])

# Same thing but a good way to check if max heap is working
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

# WE CAN ALSO BUILD A HEAP FROM INITIAL VALUES
arr = [1, 3, 2, 4, 5, 8] #linear time

heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))

print('\n----------------------------------------------')
print('FUNCTIONS -- They use def')
print('----------------------------------------------') 
def myFunc(m, n):
    return m * n
print(myFunc(3, 4))

# Nested functions have access to outer variables
# These are great for RECURSIVE problems
def outer(a, b):
    c = 'c'
    
    # Declare variables in the outer and the inner 
    # will always have access to those variables
    def inner():
        return a + b + c
    return inner()

print(outer('a', 'b'))

# With  nested functions, you can modify 
# objects but not reassign values UNLESS
# you are using nonlocal keywords
def double(arr, val):
    def helper():
        # Modifying an array works
        for i, n in enumerate(arr):
            arr[i] *= 2
            
        # Will only modify val in the helper scope
        # val *= 2 This will no work
        
        # This will modify val properly outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)
    
nums = [1, 2]
val = 3
double(nums, val)

print('\n----------------------------------------------')
print('CLASSES -- More limited but always needs self')
print('----------------------------------------------') 
class MyClass:
    # Constructor
    # Self is passed into every method -- LIKE 'THIS' KEYWORD
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)
    
    # To create method, do not need params, just self ALWAYS
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()
           
        
        
 