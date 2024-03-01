import random
import time

print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")
print("Hello, " + name + "! Best of Luck!")
time.sleep(2)
print("The game is about to start!\nLet's play Hangman!")
time.sleep(3)


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = ["January", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "plants"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Do you want to play again? (y = yes, n = no)\n").lower()
    if play_game == "y":
        main()
    elif play_game == "n":
        print("Thanks For Playing! We Expect you back again!")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the hangman word: " + display + "\nEnter your guess: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid Input. Please enter a single letter.")
        return hangman()

    if guess in already_guessed:
        print("You have already guessed that letter. Try another one.")
        return hangman()

    already_guessed.append(guess)

    if guess in word:
        for i in range(length):
            if word[i] == guess:
                display = display[:i] + guess + display[i + 1:]
        print(display + "\n")
    else:
        count += 1
        print_hangman(count)
        print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

    if count == limit:
        print("Wrong guess. You are hanged!!!\n")
        print("The word was:", word)
        play_loop()
    elif "_" not in display:
        print("Congratulations! You have guessed the word correctly!")
        play_loop()
    else:
        hangman()


def print_hangman(count):
    stages = [  # Final stage: Head, torso, both arms, and both legs
        "   _____ \n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |    / \ \n"
        "__|__\n",
        # Head, torso, both arms, and one leg
        "   _____ \n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |    /   \n"
        "__|__\n",
        # Head, torso, and both arms
        "   _____ \n"
        "  |     | \n"
        "  |     O \n"
        "  |    /|\ \n"
        "  |       \n"
        "  |       \n"
        "__|__\n",
        # Head, torso, and one arm
        "   _____ \n"
        "  |     | \n"
        "  |     O \n"
        "  |     |\ \n"
        "  |       \n"
        "  |       \n"
        "__|__\n",
        # Head and torso
        "   _____ \n"
        "  |     | \n"
        "  |     O \n"
        "  |       \n"
        "  |       \n"
        "  |       \n"
        "__|__\n",
        # Head
        "   _____ \n"
        "  |     | \n"
        "  |       \n"
        "  |       \n"
        "  |       \n"
        "  |       \n"
        "__|__\n",
        # Initial empty stage
        ""
    ]
    print(stages[count])


main()
hangman()


