import sys
import stdio

n = int(sys.argv[1])
k = int(sys.argv[2])

# compute v as the largest power of k <= n
v = 1
while v <= n / k:
    v *= k

# cast out powers of k in decreasing order
while v > 0:
    if n < v:
        stdio.write(0)
    else:
        digit = int(n / v)
        if digit > 9 and k > 10:
            stdio.write(chr(ord('A') + (digit - 10)))
        else:
            stdio.write(digit)
        n -= v * digit
    v = int(v / k)

stdio.writeln()
