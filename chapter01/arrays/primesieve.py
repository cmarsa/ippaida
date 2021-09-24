# primesieve.py

# This program takes a command-line argument n and computes the
# number of primes less than or equal to n. To do so, it computes an
# array of booleans with isPrime[i] set to True if i is prime,
# and to False otherwise.

import sys
import stdarray
import stdio

n = int(sys.argv[1])

is_prime = stdarray.create1D(n + 1, True)

for i in range(2, n):
    if is_prime[i]:
        # mark multiples of i as nonprime
        for j in range(2, n//i + 1):
            is_prime[i * j] = False

# count the primes
prime_count = 0
for i in range(2, n + 1):
    if (is_prime[i]):
        prime_count += 1
stdio.writeln(prime_count)