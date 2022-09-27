from utils import get_user_guess, create_game_object, clear
from art import logo

def game():
    clear()
    print(logo)
    print("""
    Welcome to Hi-Lo!
    A guessing game where we promise not to cheat :]
    """)
    hard_mode = input("Do you want to play in hard mode? (y/n) ").lower() == "y"
    game_state = create_game_object(hard_mode)
    clear()
    print("I'm thinking of a number between 1 and 100...")
    while game_state["guesses_remaining"] > 0:
        print(f" You have {game_state['guesses_remaining']} guess(es) remaining")
        user_guess = get_user_guess()
        if user_guess == game_state["secret_number"]:
            print(f"You got it! I was thinking of the number: {game_state['secret_number']}!")
            print("You win!")
            return
        else:
            game_state["guesses_remaining"] -= 1
            print(f"You guessed: {user_guess}")
            if user_guess > game_state["secret_number"]:
                print("Hmmm, that number is bigger than my secret number.")
            else:
                print("Hmmm, that number is smaller than my secret number")
        print("")
    clear()
    print(f"That was the last guess!\nMy secret number was {game_state['secret_number']}")
    print("I win! Thank you for playing :]")

clear()
game_start = input("Would you like to play Hi-Lo?(y/n) ").lower() == "y"
while game_start:
    game()
    game_start = input("\nWould you like to play again?(y/n) ").lower() == "y"
    clear()
print("Thanks for visiting! :}")