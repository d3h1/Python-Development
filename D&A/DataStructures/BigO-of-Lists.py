my_list = [11,3,33,7]

# !These will be O(1) because it is happening at the end of the list
# my_list.pop(3)
# my_list.append(88)

print(my_list)

# These will be O(n) because reindexing needs tp occur
my_list.pop(0)
my_list.insert(0,10)

print(my_list)

