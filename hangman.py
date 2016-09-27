import random

dictionary = ['cat', 'dog', 'penguin', 'elephant', 'giraffe', 'iguana', 'parrot', 'dinosaur',
              'alligator', 'ostrich', 'zebra', 'butterfly', 'aardvark', 'bat']


def update_answer(answer, word, letter):
    index = word.find(letter)
    count = 0

    if index != -1:
        while True:
            if index >= len(word):
                break
            elif word[index] == letter:
                count += 1
                answer[index] = letter

            index += 1

    return count


def generate_answer(word):
    s = ''

    for c in word:
        s += '_,'

    result = s.split(',', len(s))

    return result


def pick_word():
    return dictionary[random.randrange(0, len(dictionary))]


def init_game():
    return


def game():
    alphabet = 'a b c d e f g h i j k l m\nn o p q r s t u v w x y z'
    gallows = "\t\t ____\n\t\t|    |\n\t\t     |\n\t\t     |\n\t\t   __|__\n"
    hangman = gallows
    word = pick_word()
    answer = generate_answer(word)
    options = alphabet
    correct = 0
    count = 0
    chances = 5
    is_playing = True

    while is_playing:
        print(hangman)
        print(options)

        # end defines ending character; default is '\n'
        print('\n\t', end='')

        for i in answer:
            print(i, end=' ')

        if correct == len(word):
            print('\n\nYou won!')

            chances = 0
        else:
            letter = input("\n\nChoose a letter: ")
            options = options.replace(letter, ' ')
            count = update_answer(answer, word, letter)

        if count == 0:
            chances -= 1
        else:
            correct += count

        if chances == 0:
            i = input("Continue playing? y/n ")

            if i == 'y' or i == 'yes':
                hangman = gallows
                word = pick_word()
                answer = generate_answer(word)
                options = alphabet
                correct = 0
                chances = 5
            elif i == 'n' or i == 'no':
                is_playing = False


game()
