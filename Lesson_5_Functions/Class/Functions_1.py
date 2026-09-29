username = ""
userhome = ""
def get_home() -> str:
    home = input("Your home: ")
    print(f"{userhome}")
    return home

def get_name() -> str:
    name = input("Your name: ")
    print(f"{username}")
    return name

name = get_name()
home = get_home()

def greet(name :str, /, home :str = "the moon"):
    print(f"Hi {name}! I`ve never been to {home}.")

print(f"name= {name}, home = {home}")
greet(name)

""" 
def avg_temp(*args: tuple):
    total = 0.0
    for item in args:
        total += item
    average = total/ len(args)
    print(f"Avrg temp: {average}")

avg_temp(3, 8.3, 55, 38)
"""

"""

def configure_laptop(brand: str, size, /, **kwargs: dict):
    print(f"Your {brand} {size} inch laptop conf will be :")

    for k, v in kwargs.items():
        print(f" {k}: {v}")

configure_laptop("HP", "13", RAM = "24GB", processor = "Intel")
configure_laptop("Apple", "16", processor = "M4", RAM = "16GB", display = "Retina 15")
"""

