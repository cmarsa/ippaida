import sys
import stdio
from copy import copy

h = int(sys.argv[1])

for i in range(1, h + 1):
    for j in range(1, h + 1):
        # print(i, j)
        if j > i: 
            m = copy(j)
            n = copy(i)
        else:
            m = copy(i)
            n = copy(j)
        while m > 0:
            if m % n == 0:
                gcd = n
                break
            else:
                remainder = m % n
                m = n
                n = remainder
        if gcd == 1:
            stdio.write('*')
        else:
            stdio.write(' ')
        stdio.write(' ')
    stdio.writeln(' ')