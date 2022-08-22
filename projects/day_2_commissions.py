username = input("Enter your name: ")
sales = float(input("Enter your sales value ($): "))

commission = round(sales * 0.13, 2)

print(f"{username}, your commission value is: ${commission}")
