num = [23,45,12,56,12]
print(f"Before sort: {num}")

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i] 
        
print(f"After sort: {num}")

###

num.sort()
print(num)