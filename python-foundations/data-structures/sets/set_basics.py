# Creating a set

numbers = {1, 2, 3, 4}

print("Set:", numbers)

print("------------------")


# Removing duplicates using set

numbers = [1, 2, 2, 3, 3, 4, 5, 5]

unique_numbers = set(numbers)

print("Unique Elements:", unique_numbers)

print("------------------")


# Membership checking in set

numbers = {1, 2, 3, 4, 5}

if 3 in numbers:

    print("Element Found")

else:

    print("Element Not Found")

print("------------------")


# Adding elements to set

numbers = {1, 2, 3}

numbers.add(4)

print("After Adding:", numbers)

print("------------------")


# Removing elements from set

numbers = {1, 2, 3, 4}

numbers.remove(3)

print("After Removing:", numbers)

print("------------------")


# Traversing a set

numbers = {10, 20, 30, 40}

for num in numbers:

    print(num)

print("------------------")


# Length of set

numbers = {1, 2, 3, 4, 5}

print("Length of Set:", len(numbers))

print("------------------")


# Clearing a set

numbers = {1, 2, 3}

numbers.clear()

print("After Clear:", numbers)

print("------------------")


# Copying a set

numbers = {1, 2, 3}

new_set = numbers.copy()

print("Copied Set:", new_set)

print("------------------")


# Creating empty set

empty_set = set()

print("Empty Set:", empty_set)