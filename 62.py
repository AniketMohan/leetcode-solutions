# 1 <= m, n <= 100
import math

# 2026-02-12 16:12 edit: THIS BEAT 100% YAYYYYY!!!
def uniquePaths(m: int, n: int) -> int:
    if n > m:
        swap = m
        m = n
        n = swap
    m = m - 1
    n = n - 1
    n_factorial = math.factorial(n)
    answer = 1
    while n > 0:
        answer *= m + n
        n = n - 1
    return answer // n_factorial


# Testing
for m, n in [[3,7], [3, 2], [4, 4], [3,3],[7,7]]:
    print(m,n,uniquePaths(m,n))
