class Car:
    cars = []
    def __init__(self, brand, model, year, price_per_day, is_available = True):
        self.brand = brand
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.is_available = is_available
        

    def rent(self, days):
        if not self.is_available:
            raise ValueError("This car is not available")
        if not isinstance(days, int):
            raise ValueError("Days must be a number")
        if days <= 0:
            raise ValueError("Days must be greate than 0")

        self.is_available = False
        print(f"You succesfully rented a {self.brand} {self.model} car for {days} days")

    def return_car(self):
        if self.is_available:
            raise ValueError("This car was not rented yet")
        self.is_available = True
        print(f"You succesfully returned a {self.brand} {self.model} car")

    def calculate_price(self, days):
        if not isinstance(days, int):
            raise ValueError("Days must be a number")
        if days <= 0:
            raise ValueError("Days must be greate than 0")

        return days * self.price_per_day

    def show_info(self):
        return f"{self.brand}, {self.model}, {self.year} , {self.price_per_day}, {self.is_available}"


try:
    car1 = Car("BMW", "X5", 2022, 80)
    car2 = Car("Toyota", "Camry", 2020, 50)
    car3 = Car("Tesla", "Model 3", 2023, 100)

    #car1.rent(-4)
    car1.rent(6)
    car1.calculate_price(3)
    car1.return_car()
    car2.return_car()
    
except ValueError as error:
    print(f"Error: {error}")
