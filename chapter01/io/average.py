# average.py

# This program reads floats from the standard input stream until
# it reaches the end-of-file. Then it writes to standard output
# the average of those floats. From its point of view, there is
# no limit on the size of the input stream. The commands shown
# below after the first one use redirection and piping
# (discussed in the next subsection) to provide 100,000 numbers to average.py.

import stdio

total = 0.0
count = 0

while not stdio.isEmpty():
    value = stdio.readFloat()
    total += value
    count += 1
average = total / count

stdio.writeln('Average is ' + str(average))
