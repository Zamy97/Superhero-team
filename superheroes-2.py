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
        
