"""
Task 1: TEXT-BASED HANGMAN GAME
Task Description:
Design a text-based Hangman game. The program
selects a random word, and the player guesses one
letter at a time to uncover the word. You can set a
limit on the number of incorrect guesses allowed.

Features:
- 3 Levels (Easy, Medium or Hard) to choose from
- Random word generated based on level
- Life System based on level chosen

Additional Features:
- 2 Modes(Classic or Practice) to play
- API Integration for word-generation

"""

easy_words = []
medium_words = []
hard_words = []

lives = 7

def generate_word(min_length, max_length):
    pass

import random

# Word list for the game
word_list = ["python", "developer", "hangman", "puzzle", "programming", "challenge", "javascript"]

def get_random_word(word_list):
    """Selects a random word from the word list."""
    return random.choice(word_list)

def display_word_progress(word, correct_guesses):
    """Displays the current progress of the guessed word."""
    return " ".join([letter if letter in correct_guesses else "_" for letter in word])

def play_hangman():
    
    level = input("Please select a level (Easy, Medium, Hard): ")

    if level in ["Easy","easy"]:
        max_attempts = 9
    elif level in ["Medium","medium"]:
        max_attempts = 6
    elif level in ["Hard","hard"]:
        max_attempts = 3
    else:
        max_attempts = 6

    # Game setup
    word_to_guess = get_random_word(word_list)
    correct_guesses = set()
    incorrect_guesses = set()

    # Game loop
    while len(incorrect_guesses) < max_attempts and set(word_to_guess) != correct_guesses:
        print("\nWord:", display_word_progress(word_to_guess, correct_guesses))
        print(f"Incorrect guesses: {', '.join(incorrect_guesses) if incorrect_guesses else 'None'}")
        print(f"Guesses left: {max_attempts - len(incorrect_guesses)}")

        guess = input("Please pick a letter to guess: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid response.\nPlease pick a letter to guess: ")
            continue

        # Check if the letter has already been guessed
        if guess in correct_guesses or guess in incorrect_guesses:
            print("You already guessed that letter.")
            continue

        # Check if the guess is correct
        if guess in word_to_guess:
            correct_guesses.add(guess)
            print(f"Yes, '{guess}' is in the word.")
        else:
            incorrect_guesses.add(guess)
            print(f"Incorrect, '{guess}' is not in the word.")

    # Check the outcome
    if set(word_to_guess) == correct_guesses:
        print(f"\nCongratulations!\nYou've guessed the whole word: {word_to_guess}!\n\n")
    else:
        print(f"\nGame Over!\nYou couldn't guess the whole word: {word_to_guess}!\n\n")

# Start the game loop

def game_loop():

    print("Welcome to Hangman: The Text-Based Game!")
    play_variable = input("First off, do you wish to play? (Type Yes/No): ")
    
    while play_variable != "":
        if play_variable in ["Yes","yes","Y","y"]:
            play_hangman()
            play_variable = input("Do you wanna play again? (Type Yes/No): ")
        elif play_variable in ["No","no","N","n"]:
            print("\nThank you very much for playing!")
            print("See ya next time!\n")
            quit()
        else:
            print("I can't understand you!")
            play_variable = input("I asked, do you wanna play again? (Type Yes/No): ")

# Run your game loop
game_loop()