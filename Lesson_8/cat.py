class Cat:
    cat_counter = 0

    def __init__(self: Cat, mood: int = 3, hungry: int = 3, energy=3):
        self.__mood = mood
        self.__hungry = hungry
        self.__energy = energy
        Cat.cat_counter += 1

    def __del__(self: Cat):
        Cat.cat_counter

    def __str__(self: Cat):
        return f"{self.__mood}, {self.__hungry}, {self.__energy}"

    def __meow(self: Cat):
        print(f"Meowwww {Cat.cat_counter}")

    def sleep(self: Cat):
        self.__energy += 1
        self.__hungry += 1

    def feed(self: Cat):
        self.__energy += 1
        self.__mood += 1
        self.__hungry -= 1
        self.__meow()

    def play(self: Cat):
        self.__energy += 1
        self.__hungry += 1
        self.__meow()


my_cat = Cat()
my_cat.feed()
cat1 = Cat()
cat1.feed()

cat1.cat_counter = 5
cat1.feed()
