import random
from art import stages, logo
from word_list import word_list

# Prep
lives = 6
end_game = False

word = random.choice(word_list)
word_prog = []
for i  in range(len(word)):
    word_prog += ('_')
guesses = []

# Intro
print(logo)
print("GM, welcome to Hangman")

# Game loop starts
while not end_game:
    # "screen" 
    print(stages[lives])
    print(str(word_prog)) 
    if guesses:
        print("your previous guesses: " + str(guesses))
    guess = input("guess a letter: ").lower()

    if guess in guesses:
        print("you already guessed " + guess)
        continue
    guesses += guess
    for i in range(len(word)):
        if word[i] == guess:
            word_prog[i]= guess

    if guess not in word:
        lives -= 1

    if "_" not in word_prog:
        print(word_prog)
        print("GG WP")
        end_game = True
        break 

    if lives == 0:
        print(stages[lives])
        print("F")
        print("the answer was " + word )
        end_game= True
