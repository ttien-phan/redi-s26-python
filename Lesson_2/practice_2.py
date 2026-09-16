import random
"""

price = float(input("Price? "))
quantity = int(input("How many? "))

is_discount = input("Do you have a discount? ") == "Yes"

total_price = price * quantity

if is_discount:
    total_price = total_price * 0.9

print(total_price)
"""
"""
temp = float(input("What is the temp? "))
if temp < 0:
    print("It is freezing!")
elif temp <= 20 :
    print("It is cold.")
elif temp <= 30:
    print("The weather is nice.")
else:
    print("It is hot!")
"""

"""
products = []
while True: 
    name = input("What is your product name? ")
    if name == "done":
        break

    price = float(input("Price? "))
    quantity = int(input("How many?"))

    total_price = price * quantity

    products.append(total_price)

number_of_products = len(products)
total_price = sum(products)

if number_of_products > 0:
    average_price = total_price / number_of_products
else:
    average_price = 0

print("Number of products:", number_of_products)
print("Total price:", total_price)
print("Average product price:", average_price)
"""

"""
positive = 0
negative = 0
zero = 0
even = 0
odd = 0
total = 0

for i in range(10):
    number = int(input("Enter number: "))

    total += number

    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

average = total / 10

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("Total sum:", total)
print("Average:", average)
"""


"""
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Your guess? "))
    attempts +=1
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct!")
        break
print("Attemps: ", attempts)
"""

for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")