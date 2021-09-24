# couponcollector.py

# This program accepts an integer n as a command-line argument,
# and writes the number of coupons collected before obtaining one
# of each of n types. Thus it simulates a coupon collector.

import random
import sys
import stdarray
import stdio

n = int(sys.argv[1])

count = 0
collected_count = 0
is_collected = stdarray.create1D(n, False)

while collected_count < n:
    # generate another coupon
    value = random.randrange(0, n)
    count += 1
    if not is_collected[value]:
        collected_count += 1
        is_collected[value] = True
stdio.writeln(count)
