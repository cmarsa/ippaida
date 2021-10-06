# curve.py

import stddraw

n = 50
stddraw.setXscale(0, n)
stddraw.setYscale(0, n)
for i in range(n + 1):
    stddraw.line(0, n - i, i, 0)
stddraw.show()
