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

print("------------------")


# Find second largest element in tuple

numbers = (2, 4, 5, 1, 9)

large = numbers[0]

sec_large = numbers[0]

for num in numbers:

    if num > large:

        sec_large = large
        large = num

    elif num > sec_large and num != large:

        sec_large = num

print("Largest:", large)
print("Second Largest:", sec_large)

print("------------------")


# Remove duplicates from tuple

numbers = (1, 2, 2, 3, 4, 4, 5)

unique = []

for num in numbers:

    if num not in unique:

        unique.append(num)

new = tuple(unique)

print("Tuple Without Duplicates:", new)

print("------------------")


# Find frequency of elements in tuple

numbers = (1, 2, 2, 3, 2, 4)

frequency = {}

for num in numbers:

    if num in frequency:

        frequency[num] += 1

    else:

        frequency[num] = 1

print("Frequency:", frequency)

print("------------------")


# Find even and odd numbers from tuple

numbers = (1, 2, 3, 4, 5, 6)

num_even = []

num_odd = []

for num in numbers:

    if num % 2 == 0:

        num_even.append(num)

    else:

        num_odd.append(num)

print("Even Numbers:", num_even)
print("Odd Numbers:", num_odd)

print("------------------")


# Find maximum and minimum element in one loop

numbers = (4, 8, 2, 10, 1)

large = numbers[0]

small = numbers[0]

for num in numbers:

    if num > large:

        large = num

    if num < small:

        small = num

print("Maximum:", large)
print("Minimum:", small)