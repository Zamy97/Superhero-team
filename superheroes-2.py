import random

class Hero:

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = start_health
        self.current_health = starting_health
        self.abilities = list()

    def add_ability(self, ability):
        self.abilities(ability)

    def attack(self):

        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack

    def take_damage(self, damage_amount):
        self.current_health -= damage_amount

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False

    def fight(self, opponent):
        
