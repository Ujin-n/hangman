import random
import string


def start_game():
    words_list = ['python', 'java', 'kotlin', 'javascript']
    rand_word = random.choice(words_list)
    word_set = set(rand_word)
    hidden_word_list = list(len(rand_word) * '-')
    word_list = list(rand_word)
    attempts = 8
    tried_letters = set()

    while attempts > 0:
        # Show guessed letters
        print('\n')
        print(''.join(str(x) for x in hidden_word_list))

        # Letter input
        letter = input("Input a letter: > ")

        # Check if the letter has been already typed
        if letter in tried_letters:
            print("You already typed this letter")
            continue

        # Check if user typed exactly 1 letter
        if not 0 < len(letter) < 2:
            print("You should input a single letter")
            continue

        # Check if the letter is in ascii lowercase
        if letter not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
            continue

        # reveal letters or reduce attempts
        if letter in word_set and letter not in tried_letters:
            for j in range(len(word_list)):
                if word_list[j] == letter:
                    hidden_word_list[j] = letter
        elif letter in word_set and letter in tried_letters:
            print("No improvements")
            attempts -= 1
        else:
            print("No such letter in the word")
            attempts -= 1

        tried_letters.add(letter)

        if '-' not in hidden_word_list:
            print('\n')
            print(''.join(str(x) for x in hidden_word_list))
            print("You guessed the word!")
            print("You survived!")
            return

    # Printing closing message
    print("You are hanged!")


while True:
    print("H A N G M A N")
    menu_choose = input('Type "play" to play the game, "exit" to quit: > ')

    if menu_choose == 'exit':
        exit()
    elif menu_choose == 'play':
        start_game()
