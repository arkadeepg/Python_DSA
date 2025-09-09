dict1: dict= {"Value": 11}
dict2: dict = dict1

print("Value of dict2 before update:")
print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2["Value"] = 22

print("\nValue of dict2 after update:")
print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
