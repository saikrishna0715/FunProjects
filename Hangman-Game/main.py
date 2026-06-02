import random
import time
import os

hangman_figure = [
        ['-'*16],
        ['|       |'],
        ['|       |'],
        ['|        '],
        ['|        '],
        ['|        '],
        ['|        '],
        ['+++++++++++++++++']
    ]

def draw_hangman(lives=6):
    match lives:
        case 5:
            hangman_figure[3] = ['|       O']
        case 4:
            hangman_figure[4] = ['|       |']
        case 3:
            hangman_figure[4] = ['|      /|']
        case 2:
            hangman_figure[4] = ['|      /|\\']
        case 1:
            hangman_figure[5] = ['|      /']
        case 0:
            hangman_figure[5] = ['|      / \\']
        case _:
            pass

    for i in hangman_figure:
        for j in i:
            print(j)



with open(r'C:\Programming\Python\Hangman-Game\words.txt','r') as f:
    data = list(f.read().split())
    words = []
    easy_words = []
    medium_words = []
    hard_words = []
    for i in data:
        if len(i) <=5: easy_words.append(i)
        elif (len(i) >5 and len(i) < 8): medium_words.append(i)
        else: hard_words.append(i)

guess_word = ''
while 1:
    h = '''\n
    ----------------
    |        |
    |        |
    |        O
    |       /|\\
    |       / \\
    +++++++++++++++++
    '''
    print('Welcome to hangman game')
    print(h)
    user_input = input('Choose difficulty : (1,2,3) (1:Easy, 2:Medium, 3:Hard)\n')
    if user_input in ['1','2','3']:
        difficulty = int(user_input)
    else:
        print('Please a valid number. 1,2,3\n\n')
        continue

    match difficulty:
        case 1:
            words = easy_words
        case 2:
            words = medium_words
        case 3:
            words = hard_words
    guess_word = random.choice(words)
    print('Hmm...... Let me Think......')
    time.sleep(1.5)
    print('Thinking....')
    time.sleep(1.5)
    os.system('cls')
    print('..............I got a word in my Memory............')
    break

user_ans = ['_' for i in range(len(guess_word))]
wrong_assumputions = ''
guess_word = [i for i in guess_word]
chances = 6
draw_hangman(6)
while chances:
    print(f'You have {chances} Chances left to guess the word\n')
    print('Correctly Guessed Letters : ',user_ans)
    print('Wrong Assumptions :',wrong_assumputions)
    user_alphabet = input('Enter a letter : ')
    os.system('cls')
    if(len(user_alphabet) != 1):
        print('Please input one letter !!!')
        continue

    if user_alphabet in guess_word:
        positions = []
        pos = 0
        while(1):
            pos = guess_word.index(user_alphabet,pos)
            positions.append(pos)
            try:
                pos = guess_word.index(user_alphabet,pos+1)
            except ValueError as e:
                break
        for i in positions:
            user_ans[i] = user_alphabet
    else:
        if user_alphabet in wrong_assumputions:
            print('!!!!!! The letter is already guessed wrong. Please try different letter !!!!!!!')
            draw_hangman(chances)
            continue
        chances-=1
        print('!!!!!! Oops !!!!!! The Letter you\'ve entered is not in the Word')
        wrong_assumputions += str(' '+user_alphabet)
    if user_ans == guess_word:
        print('Yeahhhhhhhh You won....\nYou guessed the word correctly')
        exit()
    draw_hangman(chances)
print('Game Over')
print(f'The word is {guess_word}')