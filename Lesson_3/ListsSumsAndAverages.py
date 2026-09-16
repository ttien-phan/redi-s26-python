numbers = []
total = 0

while True: 
    num = input("Your numbers or x: ")
    
    if num.lower() == "x":
        break
    else:
        num = int(num)
        numbers.append(num)
        total += int(num)
    
average = total / len(numbers)
print("Total:", total)
print("Average:", average)
