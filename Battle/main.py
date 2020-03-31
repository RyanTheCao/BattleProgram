from character import Character, Monster, Mage
import random 


class Game:

  def __init__(self,char1,char2):

    self.char1 = char1
    self.char2 = char2    
    self.curr_turn = self.turn()

    print("Initializing battle ...")
    print("---------------------") 
    print("Welcome to the Battle.")
    print("---------------------")
    self.print_stats()
    print("")
    print(self.curr_turn.name + " gets to go first.")

  def print_stats(self):

    print(str(self.char1) + "\n" + "\n")
    print(self.char2)

  
  def game_over(self):

    if self.char1.is_dead():

      print(self.char2.name + " wins!")
      print("Game over. Thanks for playing!")

      return True

    elif self.char2.is_dead():

      print(self.char1.name + " wins!")
      print("Game over. Thanks for playing!")
      

      return True

    return False  

  def turn(self):

    player_turn = random.randint(1,2)
    curr_turn = self.char1
    if player_turn == 1:
      curr_turn = self.char1
    else:
      curr_turn = self.char2

    return curr_turn  
   

  def start_battle(self):

    while self.game_over() == False:

      input("(Press enter to continue)")
      print("------------------")
      print(self.curr_turn.name.upper() + "'S TURN")
      print("------------------")
      
      if self.curr_turn == self.char1:
        self.curr_turn.attack(self.char2)
        self.curr_turn = self.char2
      else:
        self.curr_turn.attack(self.char1)  
        self.curr_turn = self.char1

      self.print_stats()  
      print("")







ryan = Monster("Ryan")
monster = Character.factory("Monster", "Dracula")
mage = Mage("Mage")

game = Game(ryan, monster)
game.start_battle()