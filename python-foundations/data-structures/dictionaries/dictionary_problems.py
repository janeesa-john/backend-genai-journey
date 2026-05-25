# Count frequency of elements in a list

numbers = [1, 2, 2, 3, 2, 4]

frequency = {}

for num in numbers:

    if num in frequency:
        frequency[num] += 1

    else:
        frequency[num] = 1

print("Frequency Count:", frequency)

print("------------------")


# Student marks system

students = {
    "Jeni": 85,
    "Niya": 90
}

# Add new student

students["Milu"] = 88

# Update marks

students.update({"Jeni": 95})

print("Student Records:")

for name, marks in students.items():

    print(name, ":", marks)

print("------------------")


# Find student with highest marks

students = {
    "Jeni": 85,
    "Niya": 90,
    "Milu": 88
}

highest_marks = list(students.values())[0]

top_student = list(students.keys())[0]

for name, marks in students.items():

    if marks > highest_marks:

        highest_marks = marks
        top_student = name

print("Top Student:", top_student)
print("Highest Marks:", highest_marks)

print("------------------")


# Count frequency of characters in a string

message = "hello"

freq = {}

for ch in message:

    if ch in freq:
        freq[ch] += 1

    else:
        freq[ch] = 1

print("Character Frequency:", freq)

print("------------------")


# Merge two dictionaries

dict1 = {
    "name": "Janeesa"
}

dict2 = {
    "age": 27
}

dict1.update(dict2)

print("Merged Dictionary:", dict1)

print("------------------")


# Invert a dictionary

student = {
    "Jeni": 85,
    "Niya": 90
}

inverted_student = {}

for name, marks in student.items():

    inverted_student[marks] = name

print("Inverted Dictionary:", inverted_student)

print("------------------")


# Separate even and odd numbers using dictionary

numbers = [1, 2, 3, 4, 5, 6]

dict_num = {
    "even": [],
    "odd": []
}

for num in numbers:

    if num % 2 == 0:

        dict_num["even"].append(num)

    else:

        dict_num["odd"].append(num)

print("Even and Odd Groups:", dict_num)

print("------------------")


# Group words by first letter

words = ["apple", "ant", "banana", "ball"]

group = {}

for word in words:

    first = word[0]

    if first not in group:

        group[first] = []

    group[first].append(word)

print("Grouped Words:", group)

print("------------------")


# Find product with highest price

products = {
    "Laptop": 50000,
    "Phone": 30000,
    "Tablet": 25000
}

top_product = list(products.keys())[0]

highest_price = list(products.values())[0]

for product, price in products.items():

    if price > highest_price:

        highest_price = price
        top_product = product

print("Most Expensive Product:", top_product)
print("Price:", highest_price)