# musicshuffle.py

# 1.4.24 Music shuffling. You set your music player to shuffle mode.
# It plays each of the m songs before repeating any. Compose a program
# to estimate the likelihood that you will not hear any sequential
# pair of songs (that is, song 3 does not follow song 2, song 10 does
# not follow song 9, and so on).
# python musicshuffle.py 600 10000 
# 6324/10000 :  0.6324

import sys
import random
import stdio
import stdarray

m = int(sys.argv[1])
trials = int(sys.argv[2])

a = stdarray.create1D(m, 0)
for i in range(0, m):
    a[i] = i

sum_sequentials = 0
for trial in range(0, trials):
    # re-assign array
    for i in range(0, m):
        a[i] = i
    # shuffle
    for i in range(0, m):
        r = random.randrange(i, m)
        # exchange a[i] and a[r]
        temp = a[r]
        a[r] = a[i]
        a[i] = temp
    # check if there is a pair of sequetial songs
    for i in range(0, len(a)-1):
        if a[i+1] == a[i] + 1:
            sum_sequentials += 1
            break
    
stdio.writeln(str(sum_sequentials) + '/' + str(trials) + ' : ' + str(sum_sequentials*1.0/trials))