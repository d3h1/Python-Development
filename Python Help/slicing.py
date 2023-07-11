my_string = "This is my STRING!"

# Indexes in string 0 - 17
print(len(my_string) - 1)

# Slicing String
print(f"This is the sliced string: {my_string[0:7]}")
print(f"This is the sliced string: {my_string[5:7]}")

# Slicing String by Steps
print(f"This is the sliced string: {my_string[0:17:2]}")

# Reversing the String
print(f"This is the sliced string: {my_string[17:0:-2]}")

# Patrial Slicing of String
print(f"This is the sliced string: {my_string[:8]}")
print(f"This is the sliced string: {my_string[:]}")
print(f"This is the sliced string: {my_string[8:]}")


# !REVERSE STRING
print(f"This is the sliced string: {my_string[::-1]}")