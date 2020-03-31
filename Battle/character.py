import helper
import random


'''
  Implement a method in Character called factory() that accepts two arguments: "type" and "name". 
  
  If type is equal to "Monster", return a Monster with the given name, and if the type is equal to "Mage", return a Mage with the given name.
'''

class Character:
  MAX_HP = 100

  def __init__(self, name, hp, power):
    self.name = name
    self.hp = hp
    self.power = power

    if self.hp < 0 or self.hp > self.MAX_HP:
      print("ERROR: Your character is not valid.")
      exit()
    
  def lose_hp(self, amt):
    self.hp -= amt
    if self.hp < 0:
      self.hp = 0

  def is_dead(self):
    if self.hp <= 0:
      return True
    else:
      return False
      
  def attack(self, opponent):
    print(f"{self.name} attacks {opponent.name} for {self.power} damage!")
    opponent.lose_hp(self.power)

  @staticmethod
  def factory(type, name):
    if type == "Monster":
      return Monster(name)
    elif type == "Mage":
      return Mage(name)    

  def __str__(self):
    string1 = f"{self.name}'s HP:"
    string2 = f"{self.hp}/{self.MAX_HP}"
    string3 = helper.bar(self.hp, self.MAX_HP, "#")
    return helper.string3(string1, string2, string3)



# MONSTER CLASS



class Monster(Character):

  def __init__(self, name):
    super().__init__(name, 100, random.randint(1,20)) 
    
  def criticalhit(self,opponent):
    self.power = random.randint(0,30)
    opponent.lose_hp(self.power * 2)
    
  def attack(self, opponent):
    is_crit = random.randint(0,1)

    if is_crit == 0:
      self.criticalhit(opponent)
      print(f"CRITICAL HIT! {self.name} attacks {opponent.name} for {self.power * 2} damage!")
      
    else:
      super().attack(opponent)



# MAGE CLASS


class Mage(Character):

  MAX_MANA = 100  
  FIREBALL_MANA = 30
  FIREBALL_DMG = 20
  HEAL_MANA = 10        # cost of healing
  HEAL_RANGE = 0, 10    # heal between HEAL_RANGE[0] and HEAL_RANGE[1]
  SKIP_TURN_MANA = 10   # mana gain from skipping turn
  
  def __init__(self, name, hp = Character.MAX_HP, power = 10):

    self.mana = Mage.MAX_MANA
    super().__init__(name, hp, power)

  def fireball(self, opponent):

    if self.mana < Mage.FIREBALL_MANA:
      print("Not enough mana to cast fireball")
    else:
      print(f"{self.name} casts fireball! {self.name} attacks {opponent.name} for {Mage.FIREBALL_DMG} damage!")
      opponent.lose_hp(Mage.FIREBALL_DMG)
      self.mana -= Mage.FIREBALL_MANA
    
  def heal(self):

    if self.mana > self.HEAL_MANA:
      healing = random.randint(self.HEAL_RANGE[0],self.HEAL_RANGE[1]) 
      self.hp += healing 
      print(f"{self.name} healing for {healing} hp.")
    else:
      print("You do not have enough mana to heal.")

    if self.hp > Character.MAX_HP:  
      self.hp = self.MAX_HP
      
  def attack(self, opponent):
    answer = int(input(f"""
What would {self.name} like to do?
0 --> normal attack (0 mana)
1 --> fireball (- {self.FIREBALL_MANA} mana)
2 --> heal between {self.HEAL_RANGE[0]} to {self.HEAL_RANGE[1]} (- {self.HEAL_MANA}mana)
3 --> skip turn (+ {self.SKIP_TURN_MANA} mana)
"""))
    
    if answer == 0:
      super().attack(opponent)
    
    elif answer == 1:
      self.fireball(opponent)

    elif answer == 2:
      self.heal()

    elif answer == 3:
      print("You skipped your turn.")
      self.mana += 10

  def __str__(self):
    health_bar = super().__str__()
    string1 = f"{self.name}'s mana"
    string2 = f"{self.mana}/100"
    string3 = helper.bar(self.mana, self.MAX_MANA, "~")

    return (health_bar + "\n" + helper.string3(string1, string2, string3))

          