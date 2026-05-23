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

print("------------------")

# Search element in a list

numbers = [1, 2, 3, 4, 5, 6]

search = int(input("Enter a number to search: "))

if search in numbers:
    print("Element Found")

else:
    print("Element Not Found")

print("------------------")


# Reverse a list without using reverse()

l = [1, 2, 3, 4]

rev_l = []

for num in range(len(l) - 1, -1, -1):

    rev_l.append(l[num])

print("Reversed List:", rev_l)

print("------------------")


# Count occurrences of an element

numbers = [1, 2, 2, 3, 2, 4]

search = int(input("Enter a number: "))

count_num = 0

for num in numbers:

    if search == num:
        count_num += 1

print(f"{search} appears {count_num} times")

print("------------------")


# Separate even and odd numbers into different lists

numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for num in numbers:

    if num % 2 == 0:
        even.append(num)

    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)

print("------------------")


# Find common elements between two lists

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for num in list1:

    if num in list2:
        common.append(num)

print("Common elements:", common)