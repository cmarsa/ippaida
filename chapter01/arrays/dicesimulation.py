# dicesimulation.py

# The following code computes the exact probability distribution
# for the sum of two dice:
# probabilities = stdarray.create1D(13, 0.0)
# for i in range(1, 7):
#     for j in range(1, 7):
#         probabilities[i+j] += 1.0
# for k in range(2, 13):
#     probabilities[k] /= 36.0

# After this code completes, probabilities[k] is the probability
# that the dice sum to k. Run experiments to validate this calculation
# simulating n dice throws, keeping track of the frequencies of
# occurrence of each value when you compute the sum of two random
# integers between 1 and 6. How large does n have to be before your
# empirical results match the exact results to three decimal places?

# ans: n must be around 10_000_000  {python3 dicesimulation.py 10000000}

import sys
import random
import stdio
import stdarray

n = int(sys.argv[1])

theoretical_probabilities = stdarray.create1D(13, 0.0)
for i in range(1, 7):
    for j in range(1, 7):
        theoretical_probabilities[i+j] += 1.0
for k in range(2, 13):
    theoretical_probabilities[k] /= 36.0

# simulate dice throw
dice_sum = stdarray.create1D(13, 0.0)
for i in range(0, n):
    first_die = random.randint(1, 6)
    second_die = random.randint(1, 6)
    dice_sum[first_die + second_die] += 1


empirical_probabilities = stdarray.create1D(13, 0.0)
for i in range(0, len(empirical_probabilities)):
    empirical_probabilities[i] = dice_sum[i] / sum(dice_sum)

diff = stdarray.create1D(13, 0.0)
stdio.writeln('sum  theo  empir  diff')
for i in range(2, 13):
    theoretical_probabilities[i] = round(theoretical_probabilities[i], 3)
    empirical_probabilities[i] = round(empirical_probabilities[i], 3)
    diff[i] = round(theoretical_probabilities[i] - empirical_probabilities[i], 3)
    if len(str(i)) < 2:
        stdio.write(' ')
    stdio.writeln(str(i) + '  ' + str(theoretical_probabilities[i]) + '  ' + str(empirical_probabilities[i]) + '  ' + str(diff[i]))