import random
import sys
import stdio


stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])

bets = 0
wins = 0
for t in range(trials):
    # run one experiment
    cash = stake
    while (cash > 0) and (cash < goal):
        # simulate one bet
        bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1

stdio.writeln(str(100 * wins // trials) + '% wins')
stdio.writeln('AVG # bets: ' + str(bets // trials))
