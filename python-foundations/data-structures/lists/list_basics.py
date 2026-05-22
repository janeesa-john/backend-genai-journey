# Creating a shopping cart list
cart = ["Soap", "Shampoo", "Facewash"]

print("Initial Cart:", cart)

print("------------------")


# Accessing elements
print("First Item:", cart[0])
print("Second Item:", cart[1])

print("------------------")


# Updating element
cart[1] = "Conditioner"

print("Updated Cart:", cart)

print("------------------")


# Adding element
cart.append("Comb")

print("After Adding Item:", cart)

print("------------------")


# Removing element
cart.remove("Comb")

print("After Removing Item:", cart)

print("------------------")


# Iterating through list
print("Cart Items:")

for item in cart:
    print(item)

print("------------------")


# Length of list
print("Number of Items:", len(cart))