import random

print("!!!----------------> Welcome to Hangman <----------------!!!\n")
categories={1:"Sports",2:"Fruits",3:"National Geography",4:"Electronics"}
print("select category:\n1:\tSports\n2:\tFruits\n3:\tNational Geography\n4:\tElectronics\n")
sports_word = ["ball","bat","cricket","basketball"]
fruits_word = ["apple","banana","mango","orange"]
national_word = ["india","america","china","japan"]
electronics_word = ["laptop","mobile","tv","computer"]
category = int(input("Enter your choice: "))
if category == 1:
    word = random.choice(sports_word)
elif category == 2:
    word = random.choice(fruits_word)
elif category == 3:
    word = random.choice(national_word)
elif category == 4:
    word = random.choice(electronics_word)
else:
    print("Invalid choice")
    exit()

guessed_letters = []
attempts_left = 6
k = 1

while attempts_left > 0:
    # Show word progress
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    print("Current word progress: " + ' '.join(display_word))

    guess = input(f"\nEnter letter {k}: ").lower()
    k += 1

    if guess in word:
        if guess not in guessed_letters:
            guessed_letters.append(guess)
    else:
        attempts_left -= 1
        print("Wrong choice!!\nTry again!!")
        print(f"Attempts left: {attempts_left}")

    # Win condition
    if '_' not in display_word:
        print("\nWOW🌟!!!!\nYou guessed the correct word!!!!")
        break

print(f"\nThe word was: {word}")