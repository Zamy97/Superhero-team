import random

 class Ability:

     def __init__(self, name, attack_strength):
         self.name = name
         self.attack_strength = attack_strength


     def attack(self):
         lowest_possible_attack = self.attack_strength // 2
         random.randint(lowest_possible_attack,self.attack_strength)



     def update_attack(self, new_strength):
         self.attack_strength = new_strength
