# Local scope: User login system
def login():

    name = "Janeesa"
    password = 1235

    print("Logging in:", name)


login()

print("------------------")


# Global scope: Tax configuration
TAX = 18

def calculate_bill(amount):

    final = amount + (amount * (TAX / 100))

    print("Bill: Rs.", final)


amount = int(input("Enter amount: "))

calculate_bill(amount)

print("------------------")

#Non-local/ Enclosed scope: Order Tracking System
def order():

    status = "Preparing"

    def update():

        nonlocal status
        status = 'Delivered'
        print("Inside:", status)

    update()

    print("Outside:", status)

order()

print("------------------")

#Built-in scope: Student Marks System
marks = [78, 85, 90, 88]

print("Total:", sum(marks))
print("Highest:", max(marks))
print("Number of subjects:", len(marks))