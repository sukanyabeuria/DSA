income = int (input("Enter your income:"))
if income <= 250000:
   tax = 0
elif income <=500000:
  tax = 0.5 *income
elif income <=1000000:
  tax = 0.20 *income
else:
  tax = 0.30 *income
print("Your tax is:", tax) 