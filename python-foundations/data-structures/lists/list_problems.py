# Find the largest number in a list

num_list = [8, 4, 5, 2, 1, 0]

large = num_list[0]

for num in num_list:

    if num > large:
        large = num

print("Largest number:", large)

print("------------------")


# Find the smallest number in a list

small = num_list[0]

for num in num_list:

    if num < small:
        small = num

print("Smallest number:", small)

print("------------------")


# Find the sum of list elements

total = 0

for num in num_list:
    total += num

print("Sum of elements:", total)

print("------------------")


# Count even and odd numbers

even_count = 0
odd_count = 0

for num in num_list:

    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)

print("------------------")


# Remove duplicates from a list

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_list = []

for num in numbers:

    if num not in unique_list:
        unique_list.append(num)

print("Unique list:", unique_list)

print("------------------")


# Find the second largest number in a list

numbers = [2, 5, 8, 1, 0]

large = numbers[0]
sec_large = numbers[0]

for num in numbers:

    if num > large:

        sec_large = large
        large = num

    elif num > sec_large and num != large:

        sec_large = num

print("Second Largest:", sec_large)