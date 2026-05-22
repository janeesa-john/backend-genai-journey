# Using print()

def calculate_bill(price1, price2):

    total = price1 + price2

    print("Total:", total)

calculate_bill(100, 200)

print("------------------")

# Using return

def calculate_bill(price1, price2):

    total = price1 + price2

    return total


result = calculate_bill(100, 200)

print("Total:", result)

print("------------------")

# Reusing returned value

def calculate_marks(mark1, mark2, mark3):

    total = mark1 + mark2 + mark3

    return total


result = calculate_marks(78, 85, 90)

average = result / 3

print("Total Marks:", result)
print("Average:", average)

print("------------------")