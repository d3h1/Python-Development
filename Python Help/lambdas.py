# they return data, it is a good practice to assign them to a variable

triple = lambda num : num * 3  # Assigning the lambda to a variable

print(triple(10))  # Calling the lambda and giving it a parameter

concat_strings = lambda a, b, c: a[1] + b[0] + c[1]

print(concat_strings("World", "Wide", "Web"))

# ! A lambda cannot have a multi-line expression. This means that our expression needs to be something that can be written in a single line.
my_func = lambda num: "High" if num > 50 else "Low"

print(my_func(60))

#* Lambdas are really useful when a function requires another function as its argument.