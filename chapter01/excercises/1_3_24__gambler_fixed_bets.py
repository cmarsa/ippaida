import random
import sys
import stdio


stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])
max_bets = int(sys.argv[4])

bets = 0
wins = 0
agg_cash = stake
for t in range(trials):
    # run one experiment
    cash = stake
    curr_bets = 0
    while (cash > 0) and (cash < goal):
        # simulate one bet
        bets += 1
        curr_bets += 1
        if random.randrange(0, 2) == 0:
            cash += 1
        else:
            cash -= 1
        if curr_bets >= max_bets:
            break
    if cash == goal:
        wins += 1
    agg_cash += cash

stdio.writeln(str(100 * wins // trials) + '% wins')
stdio.writeln('AVG # bets: ' + str(bets // trials))
stdio.writeln('Expected Cash at Game end: ' + str(agg_cash // trials))