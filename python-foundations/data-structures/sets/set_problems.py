# Find common elements between two sets

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

common = set1.intersection(set2)

print(common)

print("------------------")


# Find unique elements from two sets

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

not_common = set1.symmetric_difference(set2)

print(not_common)

print("------------------")


# Find elements present only in first set

set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

new = set1.difference(set2)

print(new)

print("------------------")


# Check whether two sets are disjoint

set1 = {1, 2, 3}

set2 = {4, 5, 6}

for num in set1:

    if num in set2:

        print("Not disjoint")

        break

else:

    print("Disjoint")

print("------------------")


# Find subset without using issubset()

set1 = {1, 2}

set2 = {1, 2, 3, 4}

for num in set1:

    if num not in set2:

        print("Not subset")

        break

else:

    print("Subset")

print("------------------")


# Find superset without using issuperset()

set1 = {1, 2, 3, 4}

set2 = {1, 2}

for num in set2:

    if num not in set1:

        print("Not superset")

        break

else:

    print("Superset")

print("------------------")


# Find maximum element in set without using max()

numbers = {4, 8, 2, 10, 1}

max_num = float('-inf')

for num in numbers:

    if num > max_num:

        max_num = num

print(max_num)

print("------------------")


# Find minimum element in set without using min()

numbers = {4, 8, 2, 10, 1}

min_num = float('inf')

for num in numbers:

    if num < min_num:

        min_num = num

print(min_num)

print("------------------")


# Find sum of elements in set

numbers = {1, 2, 3, 4}

total = 0

for num in numbers:

    total += num

print("Sum:", total)

print("------------------")


# Count even and odd numbers in set

numbers = {1, 2, 3, 4, 5, 6}

even_count = 0

odd_count = 0

for num in numbers:

    if num % 2 == 0:

        even_count += 1

    else:

        odd_count += 1

print("Even Count:", even_count)

print("Odd Count:", odd_count)

print("------------------")


# Find largest even number in set

numbers = {1, 8, 3, 10, 5, 6}

large_even = float('-inf')

for num in numbers:

    if num % 2 == 0:

        if num > large_even:

            large_even = num

print(large_even)