# missingint.py

# 1.5.7 Compose a program that takes a command-line argument n,
# reads from standard input N-1 distinct integers between 1 and n,
# and determines the missing integer.


import sys
import stdio
import stdarray

n = int(sys.argv[1])

numbers = stdarray.create1D(n-1, 0)

for i in range(0, n - 1):
    numbers[i] = stdio.readInt()

for i in range(1, n):
    is_in_array = False
    for j in range(0, len(numbers)):
        if numbers[j] == i:
            is_in_array = True
    if not is_in_array:
        stdio.writeln('Missing number is ' + str(i))
