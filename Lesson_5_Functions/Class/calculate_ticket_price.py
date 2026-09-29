def calculate_ticket_price(age, number_of_tickets, student = False):
    if age < 12:
        price = 6
    elif age >=12:
        price = 8 
    else:
        price =  12

    total_price = price * number_of_tickets

    if age >= 18 and student == True:
            total_price = 12 * number_of_tickets * 0.8

    return total_price

print(calculate_ticket_price(10,2))
print(calculate_ticket_price(25,2))
print(calculate_ticket_price(25,2, student=True))