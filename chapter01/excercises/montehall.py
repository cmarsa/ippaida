# montehall.py

# Game simulation. In the 1970s game show Lets Make a Deal, a contestant
# is presented with three doors. Behind one of them is a valuable prize.
# After the con- testant chooses a door, the host opens one of the other two doors
# (never revealing the prize, of course). The contestant is then given the
# opportunity to switch to the other unopened door. Should the contestant do so?
# Intuitively, it might seem that the contestants initial choice door and the
# other unopened door are equally likely to contain the prize, so there would be
# no incentive to switch. Compose a program montehall.py to test this
# intuition by simulation. Your program should take a command-line argument n,
# play the game n times using each of the two strategies (switch or do not switch),
# and write the chance of success for each of the two strate- gies.

import sys
import random
import stdio


trials = int(sys.argv[1])  # number of trials

#                                   switching
success = 0
for i in range(0, trials):
    # Host hides prize behind 1 of 3 doors uniformly at random.
    prize  = random.randrange(0, 3)
    # Contestant selects 1 of 3 doors uniformly at random.
    choice = random.randrange(0, 3)
    # At random, host reveals an unchosen door not containing prize.
    reveal = random.randrange(0, 3)
    while (reveal == choice) or (reveal == prize):
        reveal = random.randrange(0, 3)
    # Hack to compute the remaining door which contestent switches to.
    other = 0 + 1 + 2 - reveal - choice
    # Switching leads to a win?
    if other == prize:
        success += 1

prob_win = float(success) / float(trials)
stdio.writeln('prob of winning by switching: ' + str(prob_win))


#                                not switching
success = 0
for i in range(0, trials):
    # Host hides prize behind 1 of 3 doors uniformly at random.
    prize  = random.randrange(0, 3)
    # Contestant selects 1 of 3 doors uniformly at random.
    choice = random.randrange(0, 3)
    # At random, host reveals an unchosen door not containing prize.
    reveal = random.randrange(0, 3)
    # not switching leads to a win?
    if choice == prize:
        success += 1

prob_win = float(success) / float(trials)
stdio.writeln('prob of winning by not switching: ' + str(prob_win))
