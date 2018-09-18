import random

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


class Weapen(Ability):

    def attack(self):
        return random.randint(0, self.attack_strength)



class Team:

    def __init__(self, team_name):

    """ Instantiate resources. """

        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):

    """ Add Hero Object to heroes list."""

        self.heroes.append(hero)

    def remove_hero(self, name):

    """ Remove hero from heroes list.
        If Hero isn't found return 0 """

        hero_list = 0

        # self.heroes.remove(hero)
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove()
                return
            hero_list += 1
        return 0












if __name__ == "__main__":
    hero = Hero("Spider Man")
    print(hero.attack())
    ability = Ability("Jumps", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Web Power", 500)
    hero.add_ability(new_ability)
    print(hero.attack())
