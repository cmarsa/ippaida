# twentyquestions.py

# This program generates a random integer between 1 and 1 million.
# Then it repeatedly reads user guesses from standard input.
# It writes Too low or Too high to standard output, as appropriate,
# in response to each guess. It write You win! to standard output
# and exits when the user's guess is correct. You always can get
# the program to write You win! with fewer than 20 questions.

import random
import stdio

RANGE = 1000000
secret = random.randrange(1, RANGE + 1)
stdio.write('I am thinking of a secret number between 1 and ')
stdio.writeln(RANGE)

guess = 0
while guess != secret:
    # solicit one guess and provide one answer
    stdio.write('What is your guess? ')
    guess = stdio.readInt()
    
    if (guess < secret):
        stdio.writeln('Too low')
    elif (guess > secret):
        stdio.writeln('Too high')
    else:
        stdio.writeln('You win!')
