import random

class Ability:

     def __init__(self, name, attack_strength):
         self.name = name
         self.attack_strength = attack_strength


     def attack(self):
         lowest_possible_attack = self.attack_strength // 2
         attack = random.randint(lowest_possible_attack,self.attack_strength)
         return attack



     def update_attack(self, new_strength):
         self.attack_strength = new_strength

class Hero:

    def __init__(self, name):
        self.abilities = list()
        self.name = name


    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):

        total = 0
        for each_items in self.abilities:
            total += each_items.attack()
        return total

if __name__ == "__main__":
    hero = Hero("Spider Man")
    print(hero.attack())
    ability = Ability("Jumps", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Web Power", 500)
    hero.add_ability(new_ability)
    print(hero.attack())
