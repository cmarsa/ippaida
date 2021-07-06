# useargument.py
"""
This program shows how we can control the actions of our programs: by providing an argument
on the command line. Doing so allows us to tailor the behavior of our programs. The program
accepts a command-line argument, and writes a message that uses it.
"""
import sys
import stdio


stdio.write('Hi, ')
stdio.write(sys.argv[1])
stdio.writeln('- How are you?')