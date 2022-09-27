from random import randint
def generate_number():
    """Returns an int [1, 100]"""
    return randint(1, 100)
def get_user_guess():
    """Gets user input and outputs an integer. Checks against potential bad inputs."""
    user_input = int(input("Guess a number between and including 1 - 100. Whole numbers only please.\n"))
    while not isinstance(user_input, int) and user_input > 0 and user_input <= 100:
        user_input = int(input("Incorrect input. Please enter a number from 1 - 100.\n"))
    return user_input
def create_game_object(is_hard):
    '''
    Params: is_hard - true for 5 guess game. false for 10 guess game.
    Returns a starting game object.
    Object will have the following properties:
    guesses_remaining and secret_number.
    '''
    guesses = 10
    if is_hard:
        guesses = 5
    return {
        "guesses_remaining": guesses,
        "secret_number": generate_number()
    }