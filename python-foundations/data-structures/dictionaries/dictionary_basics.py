# Creating a dictionary

student = {
    "name": "Janeesa",
    "age": 25,
    "place": "Thrissur"
}

print("Student Details:", student)

print("------------------")


# Accessing values

print("Name:", student["name"])
print("Age:", student["age"])

print("------------------")


# Updating value

student["age"] = 26

print("Updated Age:", student)

print("------------------")


# Adding new key-value pair

student["course"] = "Python Full Stack"

print("After Adding Course:", student)

print("------------------")


# Removing key-value pair

student.pop("place")

print("After Removing Place:", student)

print("------------------")


# Iterating through dictionary

print("Student Information:")

for key, value in student.items():

    print(key, ":", value)