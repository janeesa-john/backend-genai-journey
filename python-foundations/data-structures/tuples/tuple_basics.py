# Creating a tuple

student = ("Janeesa", 27, "Thrissur")

print("Student Details:", student)

print("------------------")


# Accessing tuple elements

print("Name:", student[0])
print("Age:", student[1])

print("------------------")


# Tuple length

print("Length:", len(student))

print("------------------")


# Iterating through tuple

for item in student:

    print(item)

print("------------------")


# Tuple packing

data = 10, 20, 30

print("Packed Tuple:", data)

print("------------------")


# Tuple unpacking

name, age, place = student

print("Name:", name)
print("Age:", age)
print("Place:", place)

print("------------------")


# Single element tuple

single = (5,)

print("Single Element Tuple:", single)
print("Type:", type(single))

print("------------------")


# Tuple concatenation

t1 = (1, 2)
t2 = (3, 4)

result = t1 + t2

print("Concatenated Tuple:", result)

print("------------------")


# Tuple repetition

numbers = (1, 2)

print("Repeated Tuple:", numbers * 3)

print("------------------")


# Membership checking

student = ("Janeesa", 27, "Thrissur")

print("Janeesa" in student)
print("Kochi" in student)