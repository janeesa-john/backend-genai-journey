# Dictionary methods example

student = {
    "name": "Janeesa",
    "age": 27,
    "place": "Thrissur"
}

print("Student Details:", student)

print("------------------")


# keys()

print("Keys:", student.keys())

print("------------------")


# values()

print("Values:", student.values())

print("------------------")


# items()

print("Items:", student.items())

print("------------------")


# get()

print("Name:", student.get("name"))

print("------------------")


# update()

student.update({"age": 28})

print("After Update:", student)

print("------------------")


# pop()

student.pop("place")

print("After Pop:", student)