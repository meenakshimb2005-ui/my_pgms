# hangman game

import random
print("Welcome to Hangman!")
word_list = ["wonder woman","the flash","batman","aquaman","superman","green lantern","joker","harley quinn","catwoman","robin","nightwing","batgirl","green arrow","black canary","martian manhunter"]
word = random.choice(word_list)
incorrect_guesses = 0
max_incorrect_guesses = 6
wrong_letters = []
guessed_letters = ["_"] * len(word) 
if " " in word :
    for i, letter in enumerate(word):
        if letter == " ":
            guessed_letters[i] = " "
i = 0
while incorrect_guesses < max_incorrect_guesses and "_" in guessed_letters:
    word_display = " ".join(guessed_letters)
    print(f"Word: {word_display}")
    guess = input("Guess a letter: ").lower()
    if len(guess) == len(word) and guess.isalpha():
        if guess == word:
            print(f"Congratulations! You guessed the word '{word}' correctly!")
            break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters or guess in wrong_letters:
        print("You already guessed that letter.")
        continue
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                guessed_letters[i] = guess
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        wrong_letters.append(guess)
        print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
    print(" ".join(guessed_letters))
    print(f"Wrong letters: {', '.join(wrong_letters)}")
    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! The word was '{word}'.")
        break
