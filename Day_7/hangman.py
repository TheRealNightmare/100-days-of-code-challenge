import random
from words import word_list
from ascii_art import stages,logo


print(logo)
chosen_word = random.choice(word_list)

end_of_game = False

lives = 6


display = []
for i in range(len(chosen_word)):
    display+=('_')


while not end_of_game:
    guess = input("Letter: ").lower()
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
        
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f"The word is {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    if end_of_game == False:
        print(stages[lives])
        print(display)
        print("\n")
    else:
        pass
