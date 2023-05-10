user_prompt = "Enter a todo: "
todoList = []

t1 = input(user_prompt)
t2 = input(user_prompt)
t3 = input(user_prompt)
t4 = input(user_prompt)
t5 = input(user_prompt)

todoList.extend([t1, t2, t3, t4, t5])


count = {}

for n in todoList:
    count[n] = 1 + count.get(n, 0)

# print(count) # !TESTING COUNT

print("\n")

for i, n in count.items():
    if n == 1:
        print(f"{i} occurs {n} time this number occurs in this list!")
    else:
        print(f"{i} occurs {n} times this number occurs in this list!")
