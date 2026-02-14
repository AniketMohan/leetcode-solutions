# 1 <= n <= 9
import math

# 2026-02-12 13:00 edit: THIS BEAT 100% YAYYY!!!
def getPermutation(n: int, k: int) -> str:
    k -= 1
    answer = ""
    elements = [i+1 for i in range(n)]

    while len(elements):
        factorial_n_minus_1 = math.factorial(len(elements) - 1)
        element_number = k // factorial_n_minus_1
        answer_int = elements[element_number]
        answer += str(answer_int)
        k %= factorial_n_minus_1
        del elements[element_number]

    return answer

# Testing
for n, k in [[3,3],[4,9],[3,1]]:
    print(n,k,getPermutation(n,k))
