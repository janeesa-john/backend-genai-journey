student_names = ["Janeesa", "Niya", "Milu", "Jeena"]

print("Initial List:", student_names)

print("------------------")


# append()
student_names.append("Akhil")
print("After append():", student_names)

print("------------------")


# insert()
student_names.insert(1, "Tony")
print("After insert():", student_names)

print("------------------")


# remove()
student_names.remove("Jeena")
print("After remove():", student_names)

print("------------------")


# pop()
student_names.pop(0)
print("After pop():", student_names)

print("------------------")


# sort()
student_names.sort()
print("After sort():", student_names)

print("------------------")


# reverse()
student_names.reverse()
print("After reverse():", student_names)

print("------------------")


# count()
print("Count of Niya:", student_names.count("Niya"))

print("------------------")


# index()
print("Index of Milu:", student_names.index("Milu"))