expenses = [{"Month":"January", "Expense":2200},
                  {"Month":"February", "Expense": 2350},
                  {"Month":"March", "Expense": 2600},
                  {"Month":"April", "Expense": 2130},
                  {"Month":"May", "Expense": 2190}]

desired_month = "January"

for val in expenses:
    if val["Month"] == desired_month:
        print(val["Expense"])
        break
