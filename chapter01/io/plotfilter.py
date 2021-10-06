# plotfilter.py

# This program reads x- and y-scales from standard input, and configures
# the stddraw canvas accordingly. Then it reads points from standard input
# until it reaches end-of-file, and plots them to standard drawing.
# The file usa.txt on the booksite has the coordinates of the U.S.
# cities with populations over 500. Some data, such as the data in usa.txt, is inherently visual.


import stddraw
import stdio

# read and set the x- and y-scales
x0 = stdio.readFloat()
y0 = stdio.readFloat()
x1 = stdio.readFloat()
y1 = stdio.readFloat()

stddraw.setXscale(x0, x1)
stddraw.setYscale(y0, y1)

# read and plot the points
stddraw.setPenRadius(0.0)
while not stdio.isEmpty():
    x = stdio.readFloat()
    y = stdio.readFloat()
    stddraw.point(x, y)
stddraw.show()
