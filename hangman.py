# import additional functions
from random import choice
from random_word import RandomWords
from IPython.display import clear_output

# declare game variables
r = RandomWords()
words = r.get_random_words()
word = choice(words)  # randomly chooses a word from words list
guessed, lives, game_over = [], 7, False  # multivariable assignment

# create a list of underscores
guesses = ["_ "] * len(word)

# create main fame loop
while not game_over:
    hidden_word = "".join(guesses)
    print(f"Your guessed letters: [{' '.join(sorted(guessed))}]")
    print(f'Word to guess: {hidden_word}')
    print(f'Lives: {lives}')
    ans = input("Type quit or guess a letter: ").lower()
    clear_output()
    if ans == "quit":
        print("Thanks for playing")
        game_over = True
    elif ans in word and ans not in guessed:
        print("You guessed correctly!")
        guessed.append(ans)
        for i in range(len(word)):
            if word[i] == ans:
                guesses[i] = ans
    elif ans in guessed:
        print("You already guessed that. Try again.")
    else:
        lives -= 1
        print("Incorrect, you lost a life.")
        if ans not in guessed:
            guessed.append(ans)
        if lives <= 0:
            print("You lost all your lives, you lost!")
            print("The word was: " + word.upper())
            game_over = True
            
    if word == "".join(guesses):
        clear_output()
        print(word.upper())
        print("Congratulations, you guessed it correctly!")
        game_over = True
            
