"""

Two player game for guessing words:

Player 1: Enters a secret word

Player 2: Makes letter guesses, if they guess a wrong letter

attempts are reduced by 1. For each correct guess, all letters in

in the word corresponding to the correct guess are revealed.

All incorrect guesses are printed along with remaining attempts.

Additionally, a small drawing is presented to keep it interesting.



Finally, A WIN or LOSE message is printed at the end with an option to play again.

"""

import turtle, re, os



# Setting screen and turtle specs

s = turtle.Screen()

s.title("WORD GUESSING GAME")

s.bgcolor('pink')

s.setup(500, 400)



# Turtles

# main-turtle

m_t = turtle.Turtle()

m_t.speed(10)

m_t.pu()

m_t.color('green')

m_t.ht()



# guessed word turtle

g_t = turtle.Turtle()

g_t.speed(10)

g_t.pu()

g_t.color('red')

g_t.ht()



# attempts turtle

att_t = turtle.Turtle()

att_t.speed(10)

att_t.color('black')

att_t.pu()

att_t.pu()

att_t.ht()



# car turtle

c_t = turtle.Turtle()

c_t.speed(10)

c_t.pu()

c_t.color('blue')

c_t.pensize(2)

c_t.ht()



# globals

entered_word = ''

attempts = 8

correct_guesses = ''

incorrect_guesses = 0



# setup for player to guess the word

def setup():

    # globals

    global entered_word

    global correct_guesses

    m_t.ht()

    m_t.goto(-180, 150)

    m_t.write('Guess the word:', font=("PT Serif", 16, 'italic'))

    s = '='*11 + ' PLAYER 1 ' + '='*11 

    entered_word = input(s)

    entered_word = entered_word.replace('-', '').lower()

    correct_guesses = '*'*len(entered_word)

    m_t.goto(-180, 120)

    



def mask_word():

    x_coord = -180

    for char in correct_guesses:

        m_t.write(char, font=("PT Serif", 20, 'italic'))

        x_coord += 25

        m_t.goto(x_coord, 120)



def incorrect_guess(guessed_letter):

    global incorrect_guesses

    g_t.pu()

    if incorrect_guesses == 1:

        g_t.goto(-180, -100)

        g_t.write('Wrong Guesses:', font=("PT Serif", 16, 'italic'))

    g_t.goto(-190 + 20 * incorrect_guesses, -120)

    g_t.write(guessed_letter, font=("PT Serif", 16, 'italic'))

    g_t.ht()

    draw_car(incorrect_guesses)



def draw_car(incorrect_guesses):

    c_t.pu()

    if incorrect_guesses == 1:

        c_t.goto(0,0)

        c_t.pd()

        c_t.pencolor('blue')

        c_t.fillcolor('white')

        c_t.begin_fill()

        c_t.goto(-80, 0)

        c_t.goto(-80, 60)

        c_t.goto(0, 60)

        c_t.goto(0, 0)

        c_t.end_fill()

    elif incorrect_guesses == 2:

        c_t.pd()

        c_t.pencolor('blue')

        c_t.fillcolor('white')

        c_t.begin_fill()

        c_t.goto(40, 0)

        c_t.goto(40, 35)

        c_t.goto(0, 35)

        c_t.goto(0, 0)

        c_t.end_fill()

    elif incorrect_guesses == 3 or incorrect_guesses == 4:

        if incorrect_guesses == 3:

            c_t.goto(-55, -15)

        else:

            c_t.goto(10, -15)

        c_t.fillcolor('blue')

        c_t.begin_fill()

        c_t.circle(15)

        c_t.end_fill()

    elif incorrect_guesses == 5:

        c_t.goto(10,20)

        c_t.pd()

        c_t.goto(30, 20)

        c_t.goto(30, 28)

        c_t.goto(10, 28)

        c_t.goto(10, 20)

    elif incorrect_guesses == 6:

        c_t.goto(-55, 60)

        c_t.pd()

        c_t.fillcolor('red')

        c_t.begin_fill()

        c_t.goto(-45, 60)

        c_t.goto(-45, 65)

        c_t.goto(-55, 65)

        c_t.goto(-55, 60)

        c_t.end_fill()

    elif incorrect_guesses == 7:

        c_t.goto(-60, 35)

        c_t.pd()

        c_t.pencolor('red')

        c_t.fillcolor('red')

        c_t.begin_fill()

        c_t.goto(-40, 35)

        c_t.goto(-40, 45)

        c_t.goto(-60, 45)

        c_t.goto(-60, 35)

        c_t.end_fill()

    elif incorrect_guesses == 8:

        c_t.goto(-55, 30)

        c_t.pd()

        c_t.pencolor('red')

        c_t.fillcolor('red')

        c_t.begin_fill()

        c_t.goto(-45, 30)

        c_t.goto(-45, 50)

        c_t.goto(-55, 50)

        c_t.goto(-55, 30)

        c_t.end_fill()

    

    c_t.ht()



# Setup for player 2

def player_two():

    s.tracer(0)

    global attempts, correct_guesses, incorrect_guesses

    att_t.goto(0, -180)

    att_t.write(f'You have {attempts} attempts left', font=("PT Serif", 10, 'italic'), align='center')

    att_t.ht()

    guessed_leter = input('Guess a letter: ')

    if guessed_leter not in entered_word:

        attempts -= 1

        incorrect_guesses += 1

        incorrect_guess(guessed_leter)

    else:

        indices = [i.start() for i in re.finditer(guessed_leter, entered_word)]

        for i in indices:

            try:

                correct_guesses = correct_guesses[:i] + entered_word[i] + correct_guesses[i + 1:]

            except IndexError:

                pass

        print(correct_guesses)

    for i in range(3):

        att_t.undo()

    s.update()

    





def main():

    global attempts, correct_guesses, entered_word, incorrect_guesses

    entered_word = ''

    attempts = 8

    correct_guesses = ''

    incorrect_guesses = 0

    setup()

    os.system('cls||clear')

    mask_word()

    print('\n' + '='*11 + ' PLAYER 2 ' + '='*11)

    while attempts > 0:

        player_two()

        for i in range(len(correct_guesses) * 2):

            m_t.undo()

        mask_word()

        if correct_guesses == entered_word:

            m_t.goto(0, 70)

            m_t.color('black')

            m_t.write('YOU WIN !', font=("PT Serif", 30, 'bold'), align='center')

            return

    if attempts <= 0 and (correct_guesses != entered_word):

        m_t.goto(0, 70)

        m_t.color('black')

        m_t.write('YOU LOSE!', font=("PT Serif", 30, 'bold'), align='center')

while True:

    main()

    os.system('cls||clear')

    input('Press ENTER to play again: ')

    c_t.clear()

    g_t.clear()

    att_t.clear()

    m_t.clear()

    os.system('cls||clear')

