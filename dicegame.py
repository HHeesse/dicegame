# Dicegame Samu Morsky 2016
import random
import os

# This function takes n variable in and rolls as many dice as desired
def rollDice(n):
    return sum(random.randint(1, 6) for _ in range(n))

# This function handles the prompt for new game
# If user puts anything other than enter or quit the function will
# loop back to the beginning
def newGame():
    user_input = raw_input("Would you like to play again? Press enter to play " +
        "again or write 'quit' to exit: ")
    if user_input == "":
        return
    elif user_input.lower() == "quit":
        print "Thank you for playing!"
        quit()
    else:
        newGame()    

def main():
    os.system('clear')
    while True:
        try:
            guess = int(raw_input("Hello! Try to guess the payoff of two dice: "))
        except ValueError:
            print "That is not a number, please try again"
            continue    
        payoff = rollDice(2)
        if guess == payoff:
            print "Payoff: %s , Your answer: %s. You were correct!" % (payoff, guess) 
        else: 
            print "Payoff: %s , Your answer: %s. Your guess was incorrect!" % (payoff, guess) 
        newGame()
        

if __name__ == "__main__": main()
