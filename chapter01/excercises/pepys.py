# pepys.py

# Pepys’s problem. In 1693 Samuel Pepys asked Isaac Newton which is more likely:
# getting 1 at least once when rolling a fair die six times or
# getting 1 at least twice when rolling it 12 times.
# Compose a program that could have provided Newton with a quick answer.

# it is more likely the first scenario:
# getting 1 at least once when rolling a fair die six times.

import sys
import random
import stdio

trials = int(sys.argv[1])  # number of trials

# getting 1 at least once when rolling a fair die six times 
success = 0
for i in range(0, trials):
    for i in range(0, 6):
        die = random.randint(1, 6)
        if die == 1:
            success += 1
            break

prob = float(success) / trials
stdio.writeln('prob getting 1 at least once when rolling a fair die six times   ' + str(prob))


# getting 1 at least twice when rolling it 12 times
success = 0
for i in range(0, trials):
    draw_one = 0
    for i in range(0, 12):
        die = random.randint(1, 6)
        if die == 1:
            draw_one += 1
        if draw_one >= 2:
            success += 1
            break

prob = float(success) / trials
stdio.writeln('prob getting 1 at least twice when rolling a fair die twelve times  ' + str(prob))
