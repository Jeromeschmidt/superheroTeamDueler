import random
import copy

class Ability:
    def __init__(self, name, attack_strength):
        '''Create Instance Variables:
        name:String
        max_damage: Integer
        '''
        # TODO: Instantiate the variables listed in the docstring with then
        # values passed in
        self.name = name
        self.attack_strength = attack_strength


    def attack(self):
          ''' Return a value between 0 and the value set by self.max_damage.'''
          # TODO: Use random.randint(a, b) to select a random attack value.
          # Return an attack value between 0 and the full attack.
          # Hint: The constructor initializes the maximum attack value.
          return random.randint(0, self.attack_strength)

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        # TODO: Create instance variables for the values passed in.
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and the initialized max_block strength. '''
        return random.randint(0, self.max_block)

class Hero:
    def __init__(self, name, starting_health=100):
      '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
      '''
       # TODO: Initialize instance variables values as instance variables
       # (Some of these values are passed in above,
       # others will need to be set at a starting value)
       # abilities and armors are lists that will contain objects that we can use
      self.abilities = list()
      self.armors = list()
      self.name = name
      self.starting_health = starting_health
      self.current_health = self.starting_health
      self.deaths = 0
      self.kills = 0

    def add_ability(self, ability):
        ''' Add ability to abilities list '''
        # TODO: Add ability object to abilities:List
        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        # TODO: This method should run Ability.attack() on every ability
        # in self.abilities and returns the total as an integer.
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack

    def add_armor(self, armor):
        '''Add armor to self.armors
            Armor: Armor Object
        '''
        # TODO: Add armor object that is passed in to `self.armors`
        self.armors.append(armor)

    def defend(self, damage_amt=0):
        '''Runs `block` method on each armor.
          Returns sum of all blocks
        '''
        # TODO: This method should run the block method on each armor in self.armors
        total_defend = 0
        if(self.armors != None):
            for armor in self.armors:
                total_defend += armor.block()
            return total_defend
        return 0

    def take_damage(self, damage):
      '''Updates self.current_health to reflect the damage minus the defense.
      '''
      # TODO: Create a method that updates self.current_health to the current
      # minus the the amount returned from calling self.defend(damage).
      if(damage > self.defend(damage)):
          self.current_health = self.current_health - (damage - self.defend(damage))
      else:
          self.current_health = self.current_health

    def is_alive(self):
      '''Return True or False depending on whether the hero is alive or not.
      '''
      # TODO: Check whether the hero is alive and return true or false
      if(self.current_health > 0):
        return True
      else:
        return False

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        # TODO: This method should add the number of kills to self.kills
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        ''' Update deaths with num_deaths'''
        # TODO: This method should add the number of deaths to self.deaths
        self.deaths += num_deaths

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        # TODO: This method will append the weapon object passed in as an
        # argument to self.abilities.
        # This means that self.abilities will be a list of
        # abilities and weapons.
        self.abilities.append(weapon)

    def fight(self, opponent):
      ''' Current Hero will take turns fighting the opponent hero passed in.
      '''
      if(len(self.abilities) == 0 and len(opponent.abilities) == 0):
          print("Draw")
      else:
          # TODO: Fight each hero until a victor emerges.
          while((self.is_alive() == True) and (opponent.is_alive() == True)):
              self.take_damage(opponent.attack())
              opponent.take_damage(self.attack())
          # Print the victor's name to the screen.
          if(self.is_alive()):
              print(self.name + " won! against: " + opponent.name)
              self.add_kill(1)
              opponent.add_deaths(1)
          else:
              print(opponent.name + " won! against: " + self.name)
              self.add_deaths(1)
              opponent.add_kill(1)
          # else:
          #   print("They knocked each other out!")

class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        # TODO: Use what you learned to complete this method.
        return random.randint((self.attack_strength//2), self.attack_strength)

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name
        '''
        # TODO: Implement this constructor by assigning the name and heroes, which should be an empty list
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # TODO: Implement this method to remove the hero from the list given their name.
        # else:
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        # TODO: Loop over the list of heroes and print their names to the terminal.
        for heroes in self.heroes:
            print(heroes.name)

    def add_hero(self, hero):
      '''Add Hero object to self.heroes.'''
      # TODO: Add the Hero object that is passed in to the list of heroes in
      # self.heroes
      self.heroes.append(hero)

    def attack(self, other_team):
        ''' Battle each team against each other.'''
        # TODO: Randomly select a living hero from each team and have
        # them fight until one or both teams have no surviving heroes.
        # Hint: Use the fight method in the Hero class.

        self_are_alive = copy.copy(self.heroes)
        other_team_are_alive = copy.copy(other_team.heroes)

        while(len(self_are_alive) > 0 and len(other_team_are_alive) > 0 ):
            self_champion = random.choice(self_are_alive)
            other_team_champion = random.choice(other_team_are_alive)

            self_current_deaths = self_champion.deaths
            other_team_champion_current_deaths = other_team_champion.deaths

            Hero.fight(self_champion, other_team_champion)

            if(self_champion.deaths > self_current_deaths):
                self_are_alive.remove(self_champion)
            else:
                other_team_are_alive.remove(other_team_champion)

        if(len(self_are_alive) > 0):
            print(self.name + " have defeated " + other_team.name)
        else:
            print(other_team.name + " have defeated " + self.name)

    def attack_tanks(self, other_team):
        #battles team with largest armor going first

        self_are_alive = copy.copy(self.heroes)
        other_team_are_alive = copy.copy(other_team.heroes)

        #sorted heroes by armor
        self_are_alive.sort(key=lambda self_are_alive: self_are_alive.defend(), reverse=True)
        other_team_are_alive.sort(key=lambda other_team_are_alive: other_team_are_alive.defend(), reverse=True)

        while(len(self_are_alive) > 0 and len(other_team_are_alive) > 0 ):
            self_champion = self_are_alive[0]
            other_team_champion = other_team_are_alive[0]

            self_current_deaths = self_champion.deaths
            other_team_champion_current_deaths = other_team_champion.deaths

            Hero.fight(self_champion, other_team_champion)

            if(self_champion.deaths > self_current_deaths):
                self_are_alive.remove(self_champion)
            else:
                other_team_are_alive.remove(other_team_champion)

        if(len(self_are_alive) > 0):
            print(self.name + " have defeated " + other_team.name)
        else:
            print(other_team.name + " have defeated " + self.name)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        # TODO: This method should reset all heroes health to their
        # original starting value.
        for hero in self.heroes:
            hero.current_health = health

    def stats(self):
        '''Print team statistics'''
        # TODO: This method should print the ratio of kills/deaths for each
        # member of the team to the screen.
        # This data must be output to the console.
        # Hint: Use the information stored in each hero.
        #awesome print format adopted from: https://scientificallysound.org/2016/10/17/python-print3/
        print("------------------------------------------------")
        print('{:<15s}{:>4s}{:>12s}{:>14s}'.format("Name:", "Kills:", "Deaths:", "K/D Ratio:"))
        print("------------------------------------------------")
        for hero in self.heroes:
            if(hero.deaths == 0):
                print('{:<15s}{:>4d}{:>12d}{:>15f}'.format(hero.name, hero.kills, hero.deaths, (hero.kills/1)))
            else:
                print('{:<15s}{:>4d}{:>12d}{:>15f}'.format(hero.name, hero.kills, hero.deaths, (hero.kills/hero.deaths)))
            print("------------------------------------------------")



class Arena(Team):
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
    # TODO: create instance variables named team_one and team_two that
    # will hold our teams.
        self.team_one = Team("team_one")
        self.team_two = Team("team_two")

    def create_ability(self):
        '''Prompt for Ability information.
            return Ability with values from user Input
        '''
        # TODO: This method will allow a user to create an ability.
        # Prompt the user for the necessary information to create a new ability object.
        # return the new ability object.
        ability_name = input("What would you like the new ability to be called?\n")
        ability_str = int(input("What would you like the new abilitiy's strength to be?\n"))
        new_ability = Ability(ability_name, ability_str)
        return new_ability

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        # TODO: This method will allow a user to create a weapon.
        # Prompt the user for the necessary information to create a new weapon object.
        # return the new weapon object.
        weapon_name = input("What would you like the new weapon to be called?\n")
        weapon_str = int(input("What would you like the new weapon's strength to be?\n"))
        new_weapon = Weapon(weapon_name, weapon_str)
        return new_weapon

    def create_armor(self):
        '''Prompt user for Armor information
          return Armor with values from user input.
        '''
        # TODO:This method will allow a user to create a piece of armor.
        #  Prompt the user for the necessary information to create a new armor
        #  object.
        #
        #  return the new armor object with values set by user.
        armor_name = input("What would you like the new armor to be called?\n")
        armor_str = int(input("What would you like the new armor's strength to be?\n"))
        new_armor = Armor(armor_name, armor_str)
        return new_armor


    def create_hero(self):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        # TODO: This method should allow a user to create a hero.
        # User should be able to specify if they want armors, weapons, and
        # abilities.
        # Call the methods you made above and use the return values to build
        # your hero.
        #
        # return the new hero object
        Hero_name = input("What would you like the new Hero to be called?\n")
        new_Hero = Hero(Hero_name)

        add_ability = input("Add an ability? Y or N: ")

        if add_ability.lower() == "y":
            ability = self.create_ability()
            new_Hero.add_ability(ability)

        add_weapon = input("Add an weapon? Y or N: ")

        if add_weapon.lower() == "y":
            weapon = self.create_weapon()
            new_Hero.add_weapon(weapon)

        add_armor = input("Add an armor? Y or N: ")
        if add_armor.lower() == "y":
            armor = self.create_armor()
            new_Hero.add_armor(armor)

        return new_Hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        # TODO: This method should allow a user to create team one.
        # Prompt the user for the number of Heroes on team one
        # call self.create_hero() for every hero that the user wants to add to team one.
        #
        # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        # TODO: This method should allow a user to create team two.
        # Prompt the user for the number of Heroes on team two
        # call self.create_hero() for every hero that the user wants to add to team two.
        #
        # Add the created hero to team two.
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self, which_battle=0):
        '''Battle team_one and team_two together.'''
        # TODO: This method should battle the teams together.
        # Call the attack method that exists in your team objects
        # for that battle functionality.
        if which_battle == 0:
            self.team_one.attack(self.team_two)
        else:
            self.team_one.attack_tanks(self.team_two)

    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        #     Show surviving heroes.
        # for hero in self.team_one.heroes:

        self.team_one.stats()
        self.team_two.stats()

        team_kills = 0
        team_deaths = 0

        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        team_kills = 0
        team_deaths = 0

        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))

        #display surviving heroes from each team
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)
                print(hero.name + " was rewarded " + str(random.randint(0,10000)) + " XP for surviving")
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from "+ self.team_two.name + ": " + hero.name)
                print(hero.name + " was rewarded " + str(random.randint(0,10000)) + " XP for surviving")


# if __name__ == "__main__":
#     arena = Arena()
#     arena.build_team_one()
#     arena.build_team_two()
#     arena.team_battle()
#     arena.show_stats()
# if __name__ == "__main__":
    # team_one = Team("One")
    # jodie = Hero("Jodie Foster")
    # aliens = Ability("Alien Friends", 10000)
    # jodie.add_ability(aliens)
    # team_one.add_hero(jodie)
    # team_two = Team("Two")
    # athena = Hero("Athena")
    # socks = Armor("Socks", 10)
    # athena.add_armor(socks)
    # team_two.add_hero(athena)
    # print(team_two.heroes[0].current_health)# == 100
    #
    # team_one.attack(team_two)
    #
    # print(team_two.heroes[0].current_health)# <= 0
    #
    # team_one.stats()
    # team_two.stats()
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        which_battle = int(input("Enter 0 to battle normal or enter 1 to battle tanks first: "))
        arena.team_battle(which_battle)
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False
        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
