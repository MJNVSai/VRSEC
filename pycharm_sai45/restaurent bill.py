# RESTAURENT BILL

qty = float(input("enter the quantity of the item sold: "))
cost = float(input("enter the cost of each item: "))
discount = float(input("enter the discount percentage: "))
tax = float(input("enter the value of the tax: "))

# amount calculation
amt = qty*cost

#discount calculation
discount_amount = (amt*discount)/100
sub_total = amt - discount_amount

# tax calculation
tax_amt = (sub_total*tax)/100

total_amt = sub_total + tax_amt
print()
print("*************" + '\033[91m' + " BILL " + '\033[0m' + "*************")

print("quantity of the item sold: \t",qty)
print("price of the each item:    \t",cost)
print("                          ----------------")
print("amount:                    \t",amt)
print("discount:                  \t-",discount_amount)
print("                          -----------------")
print("discounted total:          \t",sub_total)
print("tax:                       \t+",tax_amt)
print("                          ------------------")
print("Total amount to be paid:   \t",total_amt)