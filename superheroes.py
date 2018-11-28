import random

class Hero:

    def __init__(self, name, start_health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.starting_health = start_health
        self.current_health = start_health
        self.deaths = 0
        self.kills = 0



    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapen(self, weapon):
        self.abilities.append(weapon)

    def add_armor(self, armor):
        self.armors.append(armor)

    def attack(self):

        total = 0
        for each_items in self.abilities:
            total += each_items.attack()
        return total

    def defend(self):

        total_defense = 0


        if self.current_health == 0:
            return 0

        for armor in self.armors:
            armor_defense = armor.defend()
            total_defense += armor_defense

        return total_defense


         # if len(self.armors) >= 1:
         #    for armor in self.armors:
         #        if self.health == 0:
         #            return 0
         #        else:
         #            return armor.defend()
         # else: return 0


    def take_damage(self, damage_amount):

        self.current_health -= damage_amount

        if self.current_health <= 0:
            self.deaths += 1

    def add_kill(self, number_kills):
         self.kills += number_kills

class Ability:

     def __init__(self, name, attack_strength):
         self.name = name
         self.attack_strength = int(attack_strength)


     def attack(self):
# Why am I using the lowest possible attack here?
# is it necessary here?
         lowest_possible_attack = self.attack_strength // 2
         attack_value = random.randint(lowest_possible_attack,self.attack_strength)
         return attack_value


     def update_attack(self, new_strength):
         self.attack_strength = new_strength


class Weapon(Ability):

    def attack(self):
# why doesn't the tests pass when I use the lowest_possible_attack here in the random randint?
        return random.randint((self.attack_strength//2), self.attack_strength)



class Team:

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        hero_list = 0
        for hero in self.heroes:
# why am I assigning the name to the hero name?
            if hero.name == name:
                self.heroes.remove(hero)
                return   # was return 1
# Why am I adding number on the list again?
            hero_list += 1
        return 0

    def find_hero(self, name):
        """ Find and return hero from heroes list.
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
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on the each hero with the number of kills made.

        """
        total_attack = 0
        dead_enemies = 0

        for hero in self.heroes:
            total_attack += hero.attack()

        dead_enemies = other_team.defend(total_attack)

        for hero in other_team.heroes:
            hero.deaths += dead_enemies

        for hero in self.heroes:
            hero.add_kill(dead_enemies)

        return dead_enemies


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

        dead_heroes = 0
        for hero in self.heroes:
            heroes_health = hero.current_health
            if heroes_health <= 0:
                continue
            if heroes_health <= individual_damage:
                # The hero dies
                dead_heroes += 1
                hero.health = 0
            if heroes_health >= individual_damage:
                hero.current_health = hero.current_health - individual_damage

        return dead_heroes


    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        # get one of the heroes health first
        #once you access the health you need to reset it to the original health that is given to you.
        for hero in self.heroes:
            hero.current_health = hero.starting_health


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
        self.name = name
        self.defense = int(defense)

    def defend(self):
        return random.randint(0, self.defense)

class Arena:

    def __init__(self):
        '''
          Declare variables
        '''
        self.team_one = None
        self.team_two = None

    def build_team_one(self):

        team_one_name = input("What do you want to name your team: ")
        team = Team(team_one_name)
        print("Lets add some heroes to your " + team_one_name)

        building_team = True
        while building_team:

            hero_name_input = input("What do you want to name your hero: ")
            new_hero = Hero(hero_name_input)
            print("what abilities do you want to give your hero ?" + new_hero.name)

            building_abilities = True
            while building_abilities:
                ability_name = input("Name an ability you want to give your hero?")
                ability_attack_strength = input(" what attack strength should " + ability_name + "have?")
                new_ability = Ability(ability_name, ability_attack_strength)
                new_hero.add_ability(new_ability)
                abilities_finished = input.lower(("Add more abilities for your " + new_hero.name + " (Y/N) ?"))
                if abilities_finished == "y":
                    building_abilities = False
                else:
                    continue
            print("let's give some armor to your " + new_hero.name)

            building_armor = True
            while building_armor:
                armor_name = input("Name an armor for your hero: ")
                armor_defense = input("What defense score you want to give your hero's " + armor_name)
                new_armor = Armor(armor_name, armor_defense)
                building_armor_finished = input.lower(("add more armor for your " + new_hero.name + " (y/n) " ))
                if building_armor_finished == "y":
                    building_armor = False
                else:
                    team.add_hero(new_hero)

            building_team_finished = input("Done building your team? (y/n) ")
            if building_team_finished == "y":
                building_team = False

    return team







    def build_team_one(self):

        print("let's build a team to fight the other team")

        team_one_heroes = 1

        team_one_name = input("Chose a name for your first team?")
        # Whatever name they chose assign it to the team one above!
        self.team_one = Team(team_one_name)

        print("now that you are done choosing your team name let's chose a hero for your team")

        while team_one_heroes < 2:
            hero_name_input = input("Enter hero for your team: ")
        # Whatever name they chose for their hero assign it to the name_of_the_hero!
            first_hero = Hero(hero_name_input)

        #Ask users if they want to give any abilities to the heros
            input_abilities_for_your_hero = input("Do you want to give abilities to your hero? yes or no: ")
            if input_abilities_for_your_hero.lower() == "yes":
                input_abilities_for_your_hero = True
            elif input_abilities_for_your_hero.lower() == "no":
                input_abilities_for_your_hero = False

        # If the user says yes then let them input abilities that they want for their hero.

        while input_abilities_for_your_hero:
            abilities_name = input("Enter a name of the ability for your hero:")
            attack_strength_value = input("Enter a value to give attack strength to your hero: ")
        # Whatever abilities that they put in pass that in ability class as what the Ability class is expecting

            heroes_ability = Ability(abilities_name, attack_strength_value)

        # After you are done adding it to the ability class, give that ability to the hero

            first_hero.add_ability(heroes_ability)


            input_armor_yes_no = input(" Do you want to add armor to your hero? yes or no? ")


            if input_armor_yes_no.lower() == "yes":
                input_armor_yes_no = True

            elif input_armor_yes_no.lower() == "no":
                input_armor_yes_no = False

        # If they say yes then let them add the armor for their heroe.

        while input_armor_yes_no:
            input_armor_name = input("Enter an armor name that you want to give to your hero:")
            input_armor_defense = input("enter a value to defense the hero's armor: ")


        # After getting the name of the armor add it to the Ability list

            heroes_armor_from_input = Armor(input_armor_name, input_armor_defense)

        # Once you have have the armor in the Armor class give that armor to the heroes

            first_hero.add_armor(heroes_armor_from_input)

        # Let the user add the heroes in the team

            self.team_one.add_hero(first_hero)



    def build_team_two(self):

        print("let's build the second team now")

        team_two_heroes = 1

        team_two_name = input("Chose a name for your second team")

        self.team_two = Team(team_two_name)

        print("let's chose a hero for your second team")

        while team_two_heroes < 2:
            second_hero_input = inout("Enter a hero name for four team: ")

            second_hero = Hero(team_two_hero_input)


        team_two_hero_abilities_input = input("Do you want to give any abilities to the hero? yes or no?")

        if team_two_hero_abilities_input.lower() == "yes":
                second_hero_abilities_input = True

        elif second_hero_abilities_input.lower() == "no":
                second_hero_abilities_input = False

        while second_hero_abilities_input:
            second_abilities_name = input("Enter an ability name that you want to give to your hero: ")
            second_attack_strength_value = input("Enter a value to give strength to your hero:")

            second_heroes_ability = Ability(team2_abilities_name, team2_attack_strength_value)

            second_hero.add_ability(team2_heroes_ability)

        second_input_armor_yes_no = input("Do you want to give armor to your hero?")


        if team2_input_armor_yes_no.lower() == "yes":
                second_input_armor_yes_no = True

        elif team2_input_armor_yes_no.lower() == "no":
                second_input_armor_yes_no = False


        while team2_input_armor_yes_no:
            second_armor_name = input("Enter an armor name that you want to give to your hero for your second team: ")
            second_input_armor_defense = input("Enter a value to defense the hero's armo: ")

            second_heroes_armor_from_input = Armor(second_armor_name, second_input_armor_defense)

            second_hero.add_armor(second_heroes_armor_from_input)

            self.team_two.add_hero(second_hero)


    def team_battle(self):

        team_two_deaths = 0
        team_one_deaths = 0

        while team_two_deaths < len(self.team_two) or team_one_deaths < len(self.team_one):
            team_one_deaths = self.team_one.attack(self.team_two)
            team_two_deaths = self.team_two.attack(self.team_one)





        #
        # random_num = random.randint(0,1)
        #
        # if random_num == True:
        #
        #     while game_battle_one != True and game_battle_two != True:
        #         self.team_one.attack(self.team_two)
        #         game_battle_one = self.team_two.dead_heroes
        #         game_battle_two = self.team_one.dead_heroes()
        #         self.team_two.attack(self.team_one)
        #         game_battle_one = self.team_two.dead_heroes()
        #         game_battle_two = self.team_one.dead_heroes()
        # else:
        #     while game_battle_one != True and game_battle_two != True:
        #         self.team_two.attack(self.team_one)
        #         game_battle_one = self.team_one.dead_heroes()
        #         game_battle_one = self.team_two.dead_heroes()
        #         self.team_one.attack(team_two)
        #         game_battle_one = self.team_one.dead_heroes()
        #         game_battle_two = self.team_two.dead_heroes()






    def show_stats(self):

        # Why do I have two braces after the stats method??
        # How is stats method is being called here without creating an object of the Team class?
        #What is happening before the program gets to this two lines of code?
        print("Show stats for team one")
        print(self.team_one.stats())
        print("Show stats for team two")
        print(self.team_two.stats())


# myArena = Arena()
# myArena.team_battle()
# myArena.show_stats()


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()




if __name__ == "__main__":
    # hero = Hero(6)
    # print (hero.name)

    # hero_name_input = input("Enter hero for your team: ")
    # name_of_the_hero = Hero(hero_name_input)
    # print(name_of_the_hero)
    # print(44)
    # print(hero_name_input //  2)

    # attack_strength_value = input("Enter a value to give attack strength to your hero: ")
    #
    #
    # print(int(attack_strength_value) // 2)

    abilities_name = input("Enter a name of the ability for your hero:")
    attack_strength_value = input("Enter a value to give attack strength to your hero: ")


    heroes_ability = Ability(abilities_name, attack_strength_value)
    print(type(heroes_ability.attack_strength))
    print(type(heroes_ability.attack_strength))



    hero = Hero("Spider Man")
    print(hero.attack())
    ability = Ability("Jumps", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Web Power", 500)
    hero.add_ability(new_ability)
    print(hero.attack())
