import pytest
import superheroes
import random
import io
import sys

#test for draws with abilities
def test_team_attack_draw_abilities():
    team_one = superheroes.Team("One")
    tony = superheroes.Hero("Iron Man")
    blasters = superheroes.Ability("Blasters", 1000000)
    suit = superheroes.Armor("armored suit", 1)
    tony.add_ability(blasters)
    tony.add_armor(suit)
    team_one.add_hero(tony)
    team_two = superheroes.Team("Two")
    steve = superheroes.Hero("Captain America")
    kick = superheroes.Ability("Kick", 1000000)
    shield = superheroes.Armor("Shield", 1)
    steve.add_ability(kick)
    steve.add_armor(shield)
    team_two.add_hero(steve)
    assert team_one.heroes[0].current_health == 100
    assert team_two.heroes[0].current_health == 100

    team_one.attack(team_two)

    assert team_one.heroes[0].current_health <= 0
    assert team_two.heroes[0].current_health <= 0

#tests for draws with weapons
def test_team_attack_draw_weapons():
    team_one = superheroes.Team("One")
    tony = superheroes.Hero("Iron Man")
    blasters = superheroes.Weapon("Blasters", 1000000)
    suit = superheroes.Armor("armored suit", 1)
    tony.add_weapon(blasters)
    tony.add_armor(suit)
    team_one.add_hero(tony)
    team_two = superheroes.Team("Two")
    steve = superheroes.Hero("Captain America")
    kick = superheroes.Weapon("Kick", 1000000)
    shield = superheroes.Armor("Shield", 1)
    steve.add_weapon(kick)
    steve.add_armor(shield)
    team_two.add_hero(steve)
    assert team_one.heroes[0].current_health == 100
    assert team_two.heroes[0].current_health == 100

    team_one.attack(team_two)

    assert team_one.heroes[0].current_health <= 0
    assert team_two.heroes[0].current_health <= 0

# check to see if battle is draw if no hero has an ability
def test_team_attack_draw_no_abilities():
    team_one = superheroes.Team("One")
    tony = superheroes.Hero("Iron Man")
    blasters = superheroes.Ability("Blasters", 0)
    suit = superheroes.Armor("armored suit", 1)
    tony.add_ability(blasters)
    tony.add_armor(suit)
    team_one.add_hero(tony)
    team_two = superheroes.Team("Two")
    steve = superheroes.Hero("Captain America")
    kick = superheroes.Ability("Kick", 0)
    shield = superheroes.Armor("Shield", 1)
    steve.add_ability(kick)
    steve.add_armor(shield)
    team_two.add_hero(steve)
    assert team_one.heroes[0].current_health == 100
    assert team_two.heroes[0].current_health == 100

    team_one.attack(team_two)

    assert team_one.heroes[0].current_health == 100
    assert team_two.heroes[0].current_health == 100

# test to see if deaths are updated correclty if they both knock each other out
def test_team_attack_knock_each_other_out():
    team_one = superheroes.Team("One")
    tony = superheroes.Hero("Iron Man")
    blasters = superheroes.Ability("Blasters", 10000)
    suit = superheroes.Armor("armored suit", 1)
    tony.add_ability(blasters)
    tony.add_armor(suit)
    team_one.add_hero(tony)
    team_two = superheroes.Team("Two")
    steve = superheroes.Hero("Captain America")
    kick = superheroes.Ability("Kick", 10000)
    shield = superheroes.Armor("Shield", 1)
    steve.add_ability(kick)
    steve.add_armor(shield)
    team_two.add_hero(steve)
    assert team_one.heroes[0].deaths == 0
    assert team_two.heroes[0].deaths == 0

    team_one.attack(team_two)

    assert team_one.heroes[0].deaths == 1
    assert team_two.heroes[0].deaths == 1


# test to see if attack still works if only one team has a hero
def test_team_attack_only_one_hero():
    team_one = superheroes.Team("One")
    tony = superheroes.Hero("Iron Man")
    blasters = superheroes.Ability("Blasters", 10000)
    suit = superheroes.Armor("armored suit", 1)
    tony.add_ability(blasters)
    tony.add_armor(suit)
    team_one.add_hero(tony)
    team_two = superheroes.Team("Two")

    assert team_one.heroes[0].current_health == 100

    team_one.attack(team_two)

    assert team_one.heroes[0].current_health == 100
