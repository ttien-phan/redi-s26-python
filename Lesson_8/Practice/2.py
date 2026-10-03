import random

class GameCharacter:
    def __init__(self, name, health = 100, level = 1, inventory=None ):
        if health <= 0:
            raise ValueError("Health must be greater than 0")

        if level <= 0:
            raise ValueError("Level must be greater than 0")
        
        self.name = name
        self.health = health
        self.level = level

        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory


    def attack(self, enemy):
        if not isinstance(enemy, GameCharacter):
            raise ValueError("Enemy must br GameCharacter")
        if not enemy.is_alive():
            print(f"{enemy.name} is dead!")
            return 
        
        enemy.health -= random.randint(10, 30)

    def heal(self):
        if self.health < 100:
            self.health = min(self.health + 20, 100)

    def add_item(self, item):

        if not isinstance(item, str):
            raise ValueError("Item must be string")
        
        if not item.strip():
            raise ValueError("Item cannot be empty")
        
        self.inventory.append(item)

    def show_inventory(self):
        print(self.inventory)

    def is_alive(self):
        return self.health > 0

    def level_up(self):
        self.level += 1

try:
    killer = GameCharacter("killer", health = 1, level=1)
    hero = GameCharacter("hero", health=75, level=6)
    #hero.add_item("      ")
    #hero.attack(killer)
    #hero.heal()
    #hero.add_item(893)

except ValueError as error:
    print(f"Error: {error}")