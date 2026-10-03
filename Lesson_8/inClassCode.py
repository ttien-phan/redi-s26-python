class Dog:
    def __init__(self: Dog, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed

    def voice(self: Dog):
        print("Voice")

    def __str__(self: Dog) -> str:
        return f"{self.name} is a {self.breed} and is {self.age} years old" 

my_dog = Dog("Marley", 10, "Retriever")
my_dog.voice()

class Human:
    def __init__(self: Human, name: str, age: int):
        self.__name = name
        self.__age = age 

    def __str__(self: Human):
        return f"{self.__name} is {self.__age} yo " \
                f"Can vote? {self.can_vote()} Retire? {self.is_retired()}"

    def get_name(self: Human):
        return self.__name

    def get_age(self: Human):
        return self.__age

    def can_vote(self: Human) -> bool:
        return self.__age >= 18

    def is_retired(self: Human) -> bool:
        return self.__age >= 65

    def rename(self: Human, name: str):
        if isinstance(name, str) and name is not None and len(name) > 0:
            self.__name = name 

person = Human("Scott", 19)
person.rename(123455)
print(person)