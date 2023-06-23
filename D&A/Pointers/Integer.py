num1 = 11
num2 = num1

print("Num2 before it is updated: ")
print(f"Num1 is {num1}")
print(f"Num2 is {num2}")

print(f"Num1 points to {id(num1)}")
print(f"Num2 points to {id(num2)}")

num2 = 13

print("Num2 after it is updated: ")
print(f"Num1 is {num1}")
print(f"Num2 is {num2}")

print(f"Num1 points to {id(num1)}")
print(f"Num2 points to {id(num2)}")

#! This occurs becuase integers are immutable. Once it is placed in the integer, the previous integration does not affect it. 