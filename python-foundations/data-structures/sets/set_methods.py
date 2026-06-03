# add()

numbers = {1, 2, 3}

numbers.add(4)

print("After add():", numbers)

print("------------------")


# remove()

numbers = {1, 2, 3, 4}

numbers.remove(3)

print("After remove():", numbers)

print("------------------")


# discard()

numbers = {1, 2, 3, 4}

numbers.discard(5)

print("After discard():", numbers)

print("------------------")


# pop()

numbers = {10, 20, 30}

removed = numbers.pop()

print("Removed Element:", removed)

print("After pop():", numbers)

print("------------------")


# clear()

numbers = {1, 2, 3}

numbers.clear()

print("After clear():", numbers)

print("------------------")


# copy()

numbers = {1, 2, 3}

new_set = numbers.copy()

print("Copied Set:", new_set)

print("------------------")


# union()

set1 = {1, 2, 3}

set2 = {3, 4, 5}

print("Union:", set1.union(set2))

print("------------------")


# intersection()

set1 = {1, 2, 3}

set2 = {2, 3, 4}

print("Intersection:", set1.intersection(set2))

print("------------------")


# difference()

set1 = {1, 2, 3}

set2 = {2, 3, 4}

print("Difference:", set1.difference(set2))

print("------------------")


# issubset()

set1 = {1, 2}

set2 = {1, 2, 3, 4}

print("Is Subset:", set1.issubset(set2))

print("------------------")


# issuperset()

set1 = {1, 2, 3, 4}

set2 = {1, 2}

print("Is Superset:", set1.issuperset(set2))