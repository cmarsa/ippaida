import sys
import stdio

n = int(sys.argv[1])
for i in range(1, n + 1):
    # write the ith line
    for j in range(1, n + 1):
        # write the jth entry in the ith line
        if (i % j == 0) or (j % i == 0):
            stdio.write('* ')
        else:
            stdio.write('  ')
    stdio.writeln(i)
