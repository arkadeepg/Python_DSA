num1: int = 11
num2: int = num1

print("Value of num2 before update:")
print(num1)
print(num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22

print("\nValue of num2 after update:")
print(num1)
print(num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
