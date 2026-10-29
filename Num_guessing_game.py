import random

def compter_choice():
    return random.randint(1,100)



def main():
   while True:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print("You have 5 chances to guess the correct number.")

        print("Please select the difficulty level:")
        print("1. Easy (10 chances)")
        print("2. Medium (5 chances)")
        print("3. Hard (3 chances)")

        print()

        changes = 0
        level = ""
        while True:
            try:
                diffculty_leve_choice = int(input("Enter your choice: "))

                if 1 <= diffculty_leve_choice and 3 >= diffculty_leve_choice:
                    if diffculty_leve_choice == 1:
                        changes = 10
                        level = "Easy"
                    elif diffculty_leve_choice == 2:
                        changes = 5
                        level = "Medium"
                    elif diffculty_leve_choice == 3:
                        changes = 3
                        level = "Hard"
                    break
                else:
                    print("Please select diffculty level (1,2,3)")
            except ValueError:
                print("Enter a Number")    
                

        print(f"Great! You have selected the {level} difficulty level.")
        print("Let's start the game!")
        print()

        
        try:
            attempts = 0
            comp_choice = compter_choice()
            won = False
            for i in range(changes):
                    user_choice = int(input("Enter your guess: "))
                    print()
                    attempts+=1
                    if attempts == changes:
                        break
                    
                    if user_choice == comp_choice:
                        attempts+=1
                        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                        won = True
                        break
                    elif user_choice > comp_choice:
                        print(f"Incorrect! The number is less than {user_choice}.")
                    elif user_choice < comp_choice:
                        print(f"Incorrect! The number is greater than {user_choice}.")
                    
                    
        except ValueError:
                print("Please enter a valind number between (1-100)")
                    

        if not won:
            print(f"Game Over! The correct number was {comp_choice}.")

        print()
        playing = input("Would you like to play again (Y/N): ").upper()
        if playing != 'Y':
            print("Thanks for playing! Goodbye.")
            break
        print("\n" + "="*40 + "\n")


if __name__ == "__main__":
    main()