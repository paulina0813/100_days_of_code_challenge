#Step 6

import os
import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
print(f"Welcome to Hangman, you will start the game with 6 lives. Every time you guess a letter that's not in the chosen word, you will lose a life.\nOnce you run out of lives, or guess the word, the game will end.")
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("clear")
    
    if guess in display:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life!")
        if lives == 0:
            print("You lose.")
            end_of_game = True    
        print(f"You have {lives} lives left!")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
                
    print(stages[lives])