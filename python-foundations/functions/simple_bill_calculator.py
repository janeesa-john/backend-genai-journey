# Function to calculate total bill

def calculate(price1, price2, price3):
    total = price1 + price2 + price3
    return total

price1 = int(input("Enter product price: "))
price2 = int(input("Enter product price: "))
price3 = int(input("Enter product price: "))

result = calculate(price1, price2, price3)

print("Total:", result)