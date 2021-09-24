# iscbchecksum.py

import stdio
import sys

# get number from terminal
n = sys.argv[1]

# assert number is 9 digits long
if len(n) != 9:
    raise ValueError, 'Please enter a 9-digit integer'

# compute cumulative sum until 9th digit
cum_sum = 0
for i in range(0, 9):
    cum_sum += (10 - i) * int(n[i])
    
# compute 10nth digit of isbn, this mus suffice
# cum_sum + x = n * 11, for some integer n, this means
# cum_sum + x is a multiple of 11 (or it is divisible by 11)
for i in range(0, 11):
    if (cum_sum + i) % 11 == 0:
        checksum = i

if checksum == 10:
    checksum = 'X'
else:
    checksum = str(checksum)

# print isbn number
isbn = n + checksum

stdio.writeln(isbn)