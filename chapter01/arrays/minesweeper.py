# minesweeper.py

# 1.4.31 Minesweeper. Compose a program that takes three command-line
# arguments m, n, and p and produces an m-by-n boolean array where
# each element is occupied with probability p. In the minesweeper game,
# occupied cells represent bombs and empty cells represent safe cells.
# Write the array using an asterisk for bombs and a period for safe cells.
# Then, replace each safe square with the number of neighboring bombs
# (above, below, left, right, or diagonal) and write the result, as in this example.

#       * * . . .   * * 1 0 0
#       . . . . .   3 3 2 0 0
#       . * . . .   1 * 1 0 0

# Try to express your code so that you have as few special cases
# as possible to deal with, by using an (m + 2)-by-(n + 2) boolean array.

import sys
import random
import stdio
import stdarray


m = int(sys.argv[1])
n = int(sys.argv[2])
p = float(sys.argv[3])

# create field of mines, adding 2 extra rows and cols
# to reduce special cases, we will put no bomb
# on the extra spaces so it won't contribute to the
# couting of mines around a specific cell
field = stdarray.create2D(m + 2, n + 2, False)

# assign a mine according to probability p
# on each cell
for i in range(1, m + 1):
    for j in range(1, n + 1):
        r = random.uniform(0, 1)
        if r <= p:
            field[i][j] = True
        else:
            field[i][j] = False

# create the marked field
field_mark = stdarray.create2D(m, n, '.')
for i in range(0, m):
    for j in range(0, n):
        if field[i + 1][j + 1]:
            # bomb in cell
            field_mark[i][j] = '*'
        else:
            # couting mines around safe cell
            mine_count = 0
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    if field[k + 1][l + 1]:
                        mine_count += 1
            field_mark[i][j] = str(mine_count)

stdarray.write2D(field_mark)
