import sys
import stdio

n = int(sys.argv[1])

for i in range(0, n):
    for j in range(0, n*2):
        if (j + i) % 2 == 0:
            stdio.write('*')
        else:
            stdio.write(' ')
    stdio.writeln('')