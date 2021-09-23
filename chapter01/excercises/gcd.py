import sys
import stdio

m = int(sys.argv[1])
n = int(sys.argv[2])

if n > m:
    temp = m
    m = n
    n = temp

while m > 0:
    stdio.writeln(str(m) + ', ' + str(n))
    if m % n == 0:
        gcd = n
        break
    else:
        remainder = m % n
        m = n
        n = remainder
stdio.writeln(gcd)