#Required Arguments
def movie_booking(customer,seat_no):

    print("Name:",customer)
    print("Seat No.:",seat_no)

movie_booking("Janeesa",10)
print("------------------")

#Keyword Arguments
def hotel_booking(name, age, place):

    print("Customer:", name)
    print("Age:", age)
    print("Place:", place)

hotel_booking(name='Jeni', age=28, place='Thrissur')
print("------------------")

#Deafult Arguments
def food_order(customer,quantity=1):

    print("Name:",customer)
    print("Items:",quantity)

food_order("Janeesa",3)
print("------------------")

#Arbitrary Positional Arguments
def shopping_bill(*bill):

    print("Bill:",*bill)
    print("Total:",sum(bill))

shopping_bill(550,200,400)
print("------------------")

#Arbitrary Keyword Arguments
def student_info(**info):

    print("Name:", info["name"])
    print("Place:", info["place"])
    print("Grade:",info['grade'])

student_info(name='Niya', grade=5, place='TSR')
print("------------------")

#Combined *args + **kwargs
def order(*products,**customer_info):

    print("Products:",*products)
    print("Name:",customer_info['name'])
    print("Place:",customer_info['place'])

order('Facewash',"Sunscreen",name = 'Milu', place = 'Thrissur')