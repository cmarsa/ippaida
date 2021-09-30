# longestplateau.py

# 1.4.21 Longest plateau. Given an array of integers, compose a program
# that finds the length and location of the longest contiguous sequence of
# equal values where the values of the elements just before and just after
# this sequence are smaller.

import sys
import stdio
import stdarray

array = [0, 1, 1, 1, 1, 0, 0, 3, 3, 3, 4, 1, 2, 2, 2, 2, 2, 9]


max_index = 0
max_length = 0
for i in range(0, len(array)-1):
    curr_length = 0
    if array[i] < array[i+1]: # this indicates us we have a climb up 
        j = i + 1
        curr_length += 1
        while j < len(array) - 2:
            while array[j] == array[j+1]: # this will count the length of the sequence
                curr_length += 1
                j +=1
            break   # when no more numbers repeat, break loop
        if array[j] > array[j+1]: # this will tell us if there is a slope down
            if curr_length > max_length:
                max_length = curr_length
                max_index = i + 1
        else: # if there is no slope down and j is the penultimate index in the array, terminate
            if j == len(array) - 2:
                break

if max_length == 1:
    stdio.writeln('No platau found on array.')
else:
    stdio.writeln('Platau found on array.')
    stdio.writeln('Repeated value: ' + str(array[max_index]))
    stdio.writeln('Begins at index: ' + str(max_index) + ' with length: ' + str(max_length))