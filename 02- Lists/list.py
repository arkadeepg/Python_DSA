# List
num = [123, 432, "strjk", 453]

#print list
print(num)
print(num[0])

#length of list
print(len(num))

#add element to list
num.append(876)
print(num)

#remove element from list
num.remove(876)
print(num)

#insert after specific element/ location
if "strjk" in num:
    for idx, val in enumerate(num):
        if val == "strjk":
            num.insert(idx+1, 876)
            break
print(num)

num[1:3] = [600]
print(num)

#sort the list
num.sort()
print(num)


##################################################


print("\n")

# List of Dictionaries
expenses = [{"Month":"January", "Expense":2200},
                  {"Month":"February", "Expense": 2350},
                  {"Month":"March", "Expense": 2600},
                  {"Month":"April", "Expense": 2130},
                  {"Month":"May", "Expense": 2190}]

print(expenses[1]["Expense"])
