import random

class Hero:

    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0


    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):

        total = 0
        for each_items in self.abilities:
            total += each_items.attack()
        return total

    def defend(self):

         if len(self.armors) >= 1:
            for armor in self.armors:
                if self.health < 1:
                    return 0
                else:
                    return armor.defend()
         else: return 0

    def take_damage(self, damage_amount):

        self.health -= damage_amount
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, number_kills):
         """
         This method should add the number of kills to self.kills

         """
         self.kills += number_kills

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

    """ Add Hero Object to heroes list."""

        self.heroes.append(Hero)

    def remove_hero(self, name):

     """ Remove hero from heroes list.
         If Hero isn't found return 0 """

        hero_list = 0


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
        print("attack running")
        """ This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on the each hero with the number of kills made.

        """
        total_attack = 0

        for hero in self.heroes:
            total_attack += hero.attack()
        dead_enemies = other_team.defend(total_attack)

        for hero in self.heroes:
            hero.add_kill(dead_enemies)

        for hero in other_team.heroes:
            hero.deaths += dead_enemies


    def defend(self, damage_amount):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """

        total_defense = 0
        for hero in self.heroes:
            total_defense += hero.defend()

        if damage_amount > total_defense:
            dead_heroes = self.deal_damage(damage_amount - total_defense)
            return dead_heroes

    def deal_damage(self, damage):

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
        # get one of the heroes health first
        #once you access the health you need to reset it to the original health that is given to you.
        for hero in self.heroes:
            hero.health = hero.start_health


    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """
        # To get ratio kills you divide kills number / heroes death chances!


        kill_ratio_list = list()
        for hero in self.heroes:
            kill_ratio = hero.kills / hero.deaths

            kill_ratio_list.append(kill_ratio)

        print(kill_ratio_list)


    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        # First you need a place to save the number of kills that you might get
        # then you need to access all the heroes so you could tell each what the kill number is
        # Then add up the kills in where you were going to save the kills
        #once it's all added up in the memory
        #return it (optional)

        total_team_killed = 0
        for hero in self.heroes:
            total_team_killed += hero.num_kills
        return total_team_killed


class Armor:

    def __init__(self, name, defense):

    #    """ Instantinate name and defence steength. """
        self.name = name
        self.defense = defense

    def defend(self):

    """ Return a random value between 0 and the initialized defend strength.
    """
        return random.randint(0, self.defense)

class Arena:

    def __init__(self):
        """
        Declare variables

        """

        self.team_one = None
        self.team_two = None

    def build_team_one(self):
        """
        This method should allow a user to build team one.

        """

    def build_team_two(self):
        """
        This method should allow a user to build team two.

        """

    def team_battle(self):
        """
        This method should continue to battle teams until one or both teams are dead.

        """

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.

        """










if __name__ == "__main__":
    hero = Hero("Spider Man")
    print(hero.attack())
    ability = Ability("Jumps", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Web Power", 500)
    hero.add_ability(new_ability)
    print(hero.attack())
