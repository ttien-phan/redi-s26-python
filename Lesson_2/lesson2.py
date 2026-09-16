price = int(input("What the price of an item: "))
quantity = int(input("How many?"))

discount = input("Do you have a discount coupon? ")
totalPrice = int((price * quantity))

if discount == "yes":
    print(totalPrice * 0.9)
else:
    print(totalPrice)


quantity = int(input("How many tickets? "))
status = input("Your membership status? ")
totalPrice = quantity * 10
if status == "Gold":
    print(totalPrice * 0,7)
elif status == "Silver":
    totalPrice = totalPrice * 0.85
    print(totalPrice)

print(totalPrice)
