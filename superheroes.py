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

    def defend(self, damage_amt):
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
            print(self.name + " won!")
          elif(opponent.is_alive()):
            print(opponent.name + " won!")
          else:
            print("They knocked each other out!")

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block of code is executed.
#
#     hero = Hero("Grace Hopper", 200)
#     shield = Armor("Shield", 50)
#     hero.add_armor(shield)
#     while(hero.is_alive is True):
#         print("test")
#         hero.take_damage(50)
#     print(hero.is_alive)
if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
