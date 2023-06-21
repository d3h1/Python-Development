def print_items(n):
  for i in range(n):
    print(i)
  
  for j in range(n):
    print(j)
    
print_items(10)

# This ran n + n or 2n times -- still comes out as O(n) as we DROP CONSTANTS