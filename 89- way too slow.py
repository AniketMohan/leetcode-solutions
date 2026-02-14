# An n-bit gray code sequence is a sequence of 2**n integers where:

# Every integer is in the inclusive range [0, 2**n - 1],
# The first integer is 0,
# An integer appears no more than once in the sequence,
# The binary representation of every pair of adjacent integers differs by exactly one bit, and
# The binary representation of the first and last integers differs by exactly one bit.
# Given an integer n, return any valid n-bit gray code sequence.

# 1 <= n <= 16
def grayCode(n: int):# -> List[int]:
    answer = []
    for i in range(2 ** n):
        element = 0
        for j in range(n):
            if (i >> j) % 4 in [1,2]:
                element += 2 ** j
        answer.append(element)
    return answer

# Testing
for n in [2,1]:
    print(n, grayCode(n))
