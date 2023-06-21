def print_items(n):
  for i in range(n):
    for j in range(n):
      print(i,j)
  
  for k in range(n):
    print(k)

print_items(10)

# ! NestedForLoop-O(n^2) + RegularForLoop-O(n) will ouput O(n^2 + n) = O(n^2) 
# ? O(n) is not dominant in bigger ranges which means wemust drop it