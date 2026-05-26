# Tuple methods example

numbers = (1, 2, 2, 3, 4, 2)

print("Tuple:", numbers)

print("------------------")


# count()

print("Count of 2:", numbers.count(2))

print("------------------")


# index()

print("Index of 3:", numbers.index(3))

print("------------------")


# Membership checking

print(4 in numbers)
print(10 in numbers)

print("------------------")


# Iterating through tuple

for num in numbers:

    print(num)