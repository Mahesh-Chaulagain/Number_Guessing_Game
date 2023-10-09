import random,os

#Global constants
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Function to check user's guess against actual answer
def check_answer(guess,answer,turns):
    """checks answer against guess. returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1 
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"you got it! the answer was {answer}")

#Make function to set difficulty
def set_difficulty():
    level = input("choose a difficulty. Type 'easy' or 'hard':")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    clear_screen()
    print("""
 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
""")
    #Choosing a random number between 1 and 100
    print("Welcome to the number guessing game")
    print("I'm thinking a number between 1 and 100.")

    answer = random.randint(1,100)
    print(f"the answer is {answer}")
    turns = set_difficulty()

    #Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess the number
        guess = int(input("Make a guess:"))
        turns = check_answer(guess,answer,turns)    #update the turns variable
        if turns == 0:
            print("you've run out of guesses,you lose.")
            return  #exit and end the function
        elif guess != answer:
            print("Guess again.")
game()


