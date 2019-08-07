# importing the necessary libaries
import random

class Game:
    """ Generic game class for playing a number guessing game against the computer.
    
    Attributes:
    myName (string) representing the name of the player
    number_range (int) representing the range of the numbers for the game
    random_number (int) generates a random number in the range of the numbers for game
    number_guesses (int) the number of guesses of the player
    guessed_number (int) the guessed number of the player
    """
    def __init__ (self, myName, number_range):

        self.myName = myName
        self.number_range = number_range
        self.random_number = random.randint(1, self.number_range)
        self.number_guesses = 0
        self.guessed_number = None
    
    def take_guess(self):
        """ Function for taking the guess of the player with the help of the input function.
            The guessed number are stored in the guessed_number attribute.
            
            Args:
                None
           
           Returns:
                    True if input was valid (integer)
                    False if input was invalid (not an integer)
        """
        print("Take a guess between 1 and {}: ".format(self.number_range))
        self.guessed_number = input()
        try:
              self.guessed_number = int(self.guessed_number)
        except ValueError:
              print("Not a valid guess. Please enter a number between {}.".format(self.number_range))
              return False
        return True
    
    def play_game(self):
        """ Function for playing the numbers games. The player has 6 guesses to guess the right number,
            then the game will be automatically terminated. The programm will give the player a hint if the number is too 
            high or too low. 
            
            Args:
                None
           
           Returns:
                    True if input was valid (integer)
                    False if input was invalid (not an integer)
        """
        while self.number_guesses < 6: # just allowing the player to take up to 6 guesses 
            if not self.take_guess():
                continue
            self.number_guesses += 1 
            
            if self.guessed_number < self.random_number:
                print("Your guess is too low")
        
            if self.guessed_number > self.random_number:
                print("Your guess is too high")
        
            if self.guessed_number == self.random_number:
                print("You guessed right! Awesome, {}".format(self.myName))
                break
        else:
            print("You guessed wrong, {}. The number I was thinking of was {}!".format(self.myName,self.random_number))
    def main():
        
        """ The main() function is the main entry point of the program. Here the player enters his name,
        makes a decicions if he wants to play and chooses the level of dificulty. 
            
            Args:
                None
           
           Returns:
                    None
        """
        print("Hello my Friend, whats your name?")
        myName = input("Enter your Name: ")
        print("Hello {}! Do you want to play a game with me?".format(myName))
  
        while True:
            answer_1 = input("Enter Yes or No: ")
            if answer_1.lower() == "yes":
                print("Great {}, I have two version of a number guessing game. Do you want to play the easy or the difficult versions?".format(myName))
                print("Type 1 for easy, 2 for difficult. Press 3 to quit: ")
                players_choice = int(input())
            
                if players_choice == 3:
                    #terminate the game
                    print("OK, maybe next time!")
                    break
            
                elif players_choice == 1:
                    #initiate the easy version of the game
                    easy_version = Game(myName,20)
                    #play the easy version of the game
                    easy_version.play_game()
                    #after the game the player is at the begining of function
                    Game.main()
                
                elif players_choice == 2:
                    #initiate the difficult version of the game
                    difficult_version = Game(myName,30)
                    #play the difficult version of the game
                    difficult_version.play_game()
                    #after the game the player is at the begining of function
                    Game.main()
            
                else:
                    print("Invalid response!")
                    continue
              
            
            elif answer_1.lower() == "no":
                print("OK, maybe next time!")
                break
    
            else:
                continue