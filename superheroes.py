import random

class Hero:

    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.death = 0
        self.kills = 0


    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):

        total = 0
        for each_items in self.abilities:
            total += each_items.attack()
        return total

    def defend(self):

        total_defence = 0
        for every_item in self.armors:
            total_defence += every_item.defense()
        return total_defence

        if self.health == 0:
            return 0


    def take_damage(self, damage_amount):

        self.health -= damage_amount
        if self.health <= 0:
            self.death += 1

    def add_kill(self, num_kills):
         """
         This method should add the number of kills to self.kills

         """
         self.kills += num_kills

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


class Weapon(Ability):

    def attack(self):
        return random.randint(0, self.attack_strength)



class Team:

    def __init__(self, team_name):

        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):

    # """ Add Hero Object to heroes list."""

        self.heroes.append(Hero)

    def remove_hero(self, name):

    # """ Remove hero from heroes list.
    #     If Hero isn't found return 0 """

        hero_list = 0

        # self.heroes.remove(hero)
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return 1
            hero_list += 1
        return 0

    def find_hero(self, name):
        """ Find and return hero from heroes listself.
        If Hero isn't found return 0
        """
        for hero in self.heroes:
            if hero.name == name:
                return hero
        return 0

    def view_all_heroes(self):
        """ Print out all heroes to the console """
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        """ This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on the each hero with the number of kills made.

        """
        total_attack = 0
        for hero in self.heros:
            total_attack += hero.attack()
        dead_enemies = other_team.defend(total_attack)

        for hero in self.heroes:
            hero.add_kill(dead_enemies)





    def defend(self, damange_amount):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """

        total_defense = 0
        for hero in self.heroes:
            total_defence += hero.defend()

        if damange_amount > total_defence:
            dead_heroes = self.deal_damage(damage_amount - total_defence)
            return dead_heroes




    def deal_damange(self, damage):

        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        individual_damage = damage // len(self.heroes)



        dead_death_heroes = 0
        for hero in self.heroes:
            heroes_health = hero.health
            if heroes_health <= 0:
                continue
            if heroes_health <= individual_damage:
                # The hero dies
                dead_death_heroes += 1
                hero.health = 0
            if heroes_health >= individual_damage:
                hero.health = hero.health - individual_damage

        return dead_death_heroes


    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """






class Armor:

    def __init__(self, name, defense):

    #    """ Instantinate name and defence steength. """
        self.name = name
        self.defense = defense

    def defend(self):

    #""" Return a random value between 0 and the initialized defend strength.
    #"""
        return random.randint(0, self.defense)














if __name__ == "__main__":
    hero = Hero("Spider Man")
    print(hero.attack())
    ability = Ability("Jumps", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Web Power", 500)
    hero.add_ability(new_ability)
    print(hero.attack())
