# longestplateau.py

# 1.4.21 Longest plateau. Given an array of integers, compose a program
# that finds the length and location of the longest contiguous sequence of
# equal values where the values of the elements just before and just after
# this sequence are smaller.

import sys
import stdio
import stdarray

array = [0, 1, 1, 0, 3, 3, 3, 4, 1, 2, 2, 2, 2, 2, 9]


max_index = 0
max_length = 0
for i in range(0, len(array)-1):
    curr_length = 0
    if array[i] < array[i+1]:
        j = i + 1
        curr_length += 1
        while j < len(array) - 2:
            while array[j] == array[j+1]:
                curr_length += 1
                j +=1
            break
        if array[j] > array[j+1]:
            if curr_length > max_length:
                max_length = curr_length
                max_index = i + 1
                if j == len(array) - 1:
                    break
        else:
            if j == len(array) - 2:
                break

stdio.writeln('Repeated value: ' + str(array[max_index]))
stdio.writeln('Begins at index: ' + str(max_index) + ' with length: ' + str(max_length))