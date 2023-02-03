#!/usr/bin/python3
"""calculates the fewest number of operations needed
to result in exactly n H characters"""

def minOperations(n):
    if n <= 0:
        return 0

    ans = 0
    i = 2
    while i * 1 <= n:
        while n % i == 0:
            ans += 1
            n /= i
        i += 1
    if n > 1:
        res += 1
    return ans

