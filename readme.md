### Hangman

This is a simple hangman program in python with words from the bitcoin bip39 english dictionary.

#### Logic flow
- Start
- Generate a random word
- Generate as many blanks as letters in word
- Game loop
  1. ask the user to guess a letter
  2. is the letter guessed in the word?
        - yes -> replace the blank with letter
          - are all blanks filled?
            - yes -> GG WP
            - no -> back to step 1
        - no -> lose a life
          - Have they run out of lives?
            - yes -> F
            - no -> back to step 1