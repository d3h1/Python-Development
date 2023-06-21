def print_items(a,b):
  for i in range(a):
    print(i)
  
  for j in range(b):
    print(j)
    
# ! You can not call this O(n) as there is an a and b not just a or b . . .
# * SO it would have to be O(a) + O(b) => O(a + b)

def print_items(a,b):
  for i in range(a):
    for j in range(b):
      print(i,j)
  
# ! You can not call this O(n^2) as there is an a and b not just a or b . . .
# * SO it would have to be O(a) * O(b) => O(a * b)
      
#FOR BOTH --- THAT IS IT, there is no more, you cannot do anymore 