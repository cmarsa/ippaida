# 1_2_19_particle_displacement.py
"""
Compose a program that takes three floats x 0 , v 0 , and t from the command
line, evaluates x 0  v 0 t − G t 2  2, and writes the result. (Note : G is the constant
9.80665. This value is the displacement in meters after t seconds when an object is
thrown straight up from initial position x 0 at velocity v 0 meters per second.)
"""
from sys import argv
import stdio

x_o = float(argv[1])
v_o = float(argv[2])
t = float(argv[3])

G = 9.80665

displacement = x_o + v_o*t - (G*t**2)/2

stdio.writeln(displacement)