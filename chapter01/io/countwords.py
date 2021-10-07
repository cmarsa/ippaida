# countwords.py

# 1.5.11 Compose a program that reads in text from standard
# input and writes the number of words in the text. For the
# purpose of this exercise, a word is a sequence of non-whitespace
# characters that is surrounded by whitespace.

import stdio

count = 0
while not stdio.isEmpty():
    s = stdio.readString()
    count += 1
stdio.writeln(count)