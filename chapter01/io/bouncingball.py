# bouncingball.py

# This program draws a bouncing ball to standard drawing.
# That is, it simulates the movement of a bouncing ball in the unit box.
# The ball bounces off the boundary according to the laws of elastic collision.
# The 20-millisecond wait period keeps the black image of the ball persistent
# on the screen, even though most of the ball's pixels alternate between
# black and white. If you modify this code to take the wait time dt as a
# command-line argument, you can control the speed of the ball.

import stddraw

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)

DT = 20.0
RADIUS = 0.15
rx = 0.480
ry = 0.860
vx = 0.015
vy = 0.023

while True:
    # update ball position and draw it here
    if abs(rx + vx) + RADIUS > 1.0:
        vx = -vx
    if abs(ry + vy) + RADIUS > 1.0:
        vy = -vy
    rx = rx + vx
    ry = ry + vy

    stddraw.clear(stddraw.GRAY)
    stddraw.filledCircle(rx, ry, RADIUS)
    stddraw.show(DT)
