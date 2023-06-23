dict1 = {"value": 11}
dict2 = dict1

print(f"{dict1}")
print(f"{dict2}")

print(f"\n{id(dict1)}")
print(f"{id(dict2)}")


dict2['value'] = 2

print(f"{dict1}")
print(f"{dict2}")

print(f"\n{id(dict1)}")
print(f"{id(dict2)}")

#! They will point to the same location as dictionaries are mutable
