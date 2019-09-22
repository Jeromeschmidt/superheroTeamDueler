import random

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
      self.current_health = starting_health
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
        if((damage_amt - total_defend) > 0):
            return damage_amt - total_defend
        else:
            return 0

    def take_damage(self, damage):
      '''Updates self.current_health to reflect the damage minus the defense.
      '''
      # TODO: Create a method that updates self.current_health to the current
      # minus the the amount returned from calling self.defend(damage).
      self.current_health = self.current_health - self.defend(damage)

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

    def fight(self, opponent):
      ''' Current Hero will take turns fighting the opponent hero passed in.
      '''
      if(len(self.abilities) == 0 and len(opponent.abilities) == 0):
          print("Draw")
      else:
          # TODO: Fight each hero until a victor emerges.
          self_attack_count = 0
          opponent_attack_count = 0
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

        self_are_alive = list()
        other_team_are_alive = list()

        self_are_alive = self.heroes
        other_team_are_alive = other_team.heroes

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
        pass


if __name__ == "__main__":
    team = Team("One")
    team2 = Team("two")
    jodie = Hero("Jodie Foster")
    yes = Hero("yes")
    spider = Hero("Spiderman")
    iron = Hero("Iron Man")
    quickness = Ability("Quickness", 1300)
    bs = Ability("Quickness", 1300)
    spider.add_ability(quickness)
    iron.add_ability(bs)
    team.add_hero(jodie)
    team.add_hero(yes)
    team2.add_hero(spider)
    team2.add_hero(iron)
    team.attack(team2)
