# Find largest element in tuple

numbers = (4, 8, 2, 10, 1)

large = numbers[0]

for num in numbers:

    if num > large:

        large = num

print("Largest Element:", large)

print("------------------")


# Find smallest element in tuple

numbers = (4, 8, 2, 10, 1)

small = numbers[0]

for num in numbers:

    if num < small:

        small = num

print("Smallest Element:", small)

print("------------------")


# Sum of tuple elements

numbers = (4, 8, 2, 10, 1)

total = 0

for num in numbers:

    total += num

print("Sum of Tuple Elements:", total)

print("------------------")


# Search element in tuple using loop

numbers = (1, 2, 3, 4, 5)

search = 3

for num in numbers:

    if num == search:

        print("Element Found")
        break

else:

    print("Element Not Found")

print("------------------")


# Search element in tuple using 'in'

numbers = (1, 2, 3, 4, 5)

search = 3

if search in numbers:

    print("Element Found")

else:

    print("Element Not Found")

print("------------------")


# Count occurrences in tuple

numbers = (1, 2, 2, 3, 2, 4)

search = 2

count_num = 0

for num in numbers:

    if num == search:

        count_num += 1

print(f"{search} appears {count_num} times")

print("------------------")


# Find common elements between tuples

tuple1 = (1, 2, 3, 4, 5)

tuple2 = (4, 5, 6, 7, 8)

common = []

for num in tuple1:

    if num in tuple2:

        common.append(num)

print("Common Elements:", common)

print("------------------")


# Convert tuple to list and list to tuple

numbers = (1, 2, 3, 4)

list_new = list(numbers)

print("Tuple to List:", list_new)

tuple_new = tuple(list_new)

print("List to Tuple:", tuple_new)

print("------------------")


# Reverse a tuple

numbers = (1, 2, 3, 4, 5)

print("Reversed Tuple:", numbers[::-1])