def print_items(n):
  for i in range(n):
    for j in range(n):
      print(i,j)

print_items(10)

# On the screen, we had n * n items printing out ... O(n*2)