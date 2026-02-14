def divide(dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0
    rectified_dividend = abs(dividend)
    rectified_divisor = abs(divisor)
    
    rectified_quotient = 0
    while rectified_dividend >= rectified_divisor:
        rectified_dividend -= rectified_divisor
        rectified_quotient += 1

    sign = 1
    if divisor * dividend < 0:
        sign = -1

    return rectified_quotient * sign

# Testing
for dividend, divisor in [[10,3], [7, -3]]:
    print(dividend, divisor, divide(dividend, divisor))
