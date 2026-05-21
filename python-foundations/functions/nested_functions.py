# Basic nested function example

def outer():
    message = input("Enter your message: ")

    def inner():

        print(message)

    inner()

outer()

print("------------------")

# User registration nested function example

def register_user():

    email = input("Enter email: ")

    def validate_email():

        if "@" in email:
            print("Valid Email")
        else:
            print("Invalid Email")

    validate_email()

    print("Registration Completed")


register_user()

print("------------------")

# Order placement nested function example

def place_order():

    amount = int(input("Enter order amount: "))

    def delivery_charge():

        if amount > 300:
            print("Free Delivery")
            print("Total:",amount)
        else:
            print("Delivery Charge: Rs.50")
            print("Total:",amount+50)

    delivery_charge()

    print("Order Placed Successfully")


place_order()

print("------------------")