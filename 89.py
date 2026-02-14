# An n-bit gray code sequence is a sequence of 2**n integers where:

# Every integer is in the inclusive range [0, 2**n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

# 1 <= n <= 16
#
# 2026-02-13 15:03 edit: BEAT 70% at 7 ms yayy
def grayCode(n: int):# -> List[int]:
    if n == 1:
        return [0,1]

    gray_code_n_minus_1 = grayCode(n - 1)
    power = 2 ** (n - 1)
    return gray_code_n_minus_1 + list(map(lambda x: x + power, gray_code_n_minus_1[::-1]))

# Testing
for n in [2,1]:
    print(n, grayCode(n))
