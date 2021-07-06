# sum_of_rolling_dice.py
"""
Compose a program that writes the sum of two random integers between
1 and 6 (such as you might get when rolling dice).
"""
import random
import stdio

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

stdio.writeln(
    die1 + die2
)