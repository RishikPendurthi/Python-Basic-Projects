import random
import hangmanstages
from word_list import word_list
#word_list = ["python", "jumble", "easy", "difficult", "answer",  "xylophone"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
display = ['_' for _ in range(len(chosen_word))]
print(display)
game_over = False
while not game_over:
    
    guessed_letter = input("Guess a letter: ").lower()
    for index in range(len(chosen_word)):
        if  chosen_word[index] == guessed_letter:
            display[index] = guessed_letter
    print(display)
        
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True 
            print("You Lose")
            
    if "_" not in display:
        game_over = True
        print("You Win")
    print(hangmanstages.stages[lives])
        
