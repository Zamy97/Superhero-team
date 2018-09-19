import pytest
import superheroes
import random
import io
import sys

# Helper Functions


def capture_console_output(function_body):
    # _io.StringIO object
    string_io = io.StringIO()
    sys.stdout = string_io
    function_body()
    sys.stdout = sys.__stdout__
    return string_io.getvalue()


def create_armor():
    armors = [
    "Calculator",
        "Laser Shield",
        "Invisibility",
        "SFPD Strike Force",
        "Social Workers",
        "Face Paint",
        "Damaskus Shield",
        "Bamboo Wall",
        "Forced Projection",
        "Thick Fog",
        "Wall of Will",
        "Wall of Walls",
        "Obamacare",
        "Thick Goo"]
    name = armors[random.randint(0, len(armors) - 1)]
    power = random.randint(23, 700000)
    return superheroes.Armor(name, power)


def create_weapon():
    weapons = [
        "Antimatter Gun",
        "Star Cannon",
        "Black Hole Ram Jet",
        "Laser Sword",
        "Laser Cannon",
        "Ion Accellerated Disc Drive",
        "Superhuman Strength",
        "Blinding Lights",
        "Ferociousness",
        "Speed of Hermes",
        "Lightning Bolts"]
    name = weapons[random.randint(0, len(weapons) - 1)]
    power = random.randint(27, 700000)
    return superheroes.Weapon(name, power)


def create_ability():
    abilities = [
        "Alien Attack",
         "Science",
        "Star Power",
        "Immortality",
        "Grandmas Cookies",
        "Blinding Strength",
        "Cute Kittens",
        "Team Morale",
        "Luck",
        "Obsequious Destruction",
        "The Kraken",
        "The Fire of A Million Suns",
        "Team Spirit",
        "Canada"]
    name = abilities[random.randint(0, len(abilities) - 1)]
    power = random.randint(45, 700000)
    return superheroes.Ability(name, power)


def create_hero(weapons=False, armors=False, health=False):

    heroes = [
        "Athena",
        "Jodie Foster",
        "Christina Aguilera",
        "Gamora",
        "Supergirl",
        "Wonder Woman",
        "Batgirl",
        "Carmen Sandiego",
        "Okoye",
        "America Chavez",
        "Cat Woman",
        "White Canary",
        "Nakia",
        "Mera",
        "Iris West",
        "Quake",
        "Wasp",
        "Storm",
        "Black Widow",
        "San Luis Obispo",
        "Ted Kennedy",
        "San Francisco",
        "Bananas"]
    name = heroes[random.randint(0, len(heroes) - 1)]
    if health:
        power = health
    else:
        power = random.randint(3, 700000)
    hero = superheroes.Hero(name, power)
    if weapons and armors:
        for weapon in weapons:
            hero.add_ability(weapon)
        for armor in armors:
            hero.add_armor(armor)
    if armors and not weapons:
        for armor in armors:
            hero.add_armor(armor)

    return hero


def create_team(heroes=[]):
    teams = [
        "Orchids",
        "Red",
        "Blue",
        "Cheese Steaks",
        "Warriors",
        "49ers",
        "Marvel",
        "DC",
        "Rat Pack",
        "The Little Red Riding Hoods",
        "Team One",
        "Generic Team",
        "X-men",
        "Team Two",
        "Golden Champions",
        "Vegan Protectors",
        "The Cardinals",
        "Winky Bears",
        "Steelsmiths",
        "Boilermakers",
        "Nincompoops"]
    name = teams[random.randint(0, len(teams) - 1)]
    team = superheroes.Team(name)
    if len(heroes) > 0:
        for member in heroes:
            team.add_hero(member)
