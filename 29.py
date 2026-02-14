def number_of_bits(number: int) -> int:
    num = 1
    while number != 1:
        number = number >> 1
        num += 1
    return num

# Basically implementing LONG DIVISION(in binary tho), because repeated subtraction was too slow
def divide(dividend: int, divisor: int) -> int:
    rectified_dividend = abs(dividend)
    rectified_divisor = abs(divisor)

    if rectified_divisor > rectified_dividend:
        return 0

    quotient = 0
    power_to_check =  number_of_bits(rectified_dividend) - number_of_bits(rectified_divisor)
    while power_to_check >= 0:
        digit_place_value = 1 * 2 ** power_to_check
        resultant = digit_place_value * rectified_divisor
        if resultant <= rectified_dividend:
            rectified_dividend -= resultant
            quotient += digit_place_value
        power_to_check -= 1
    if (dividend > 0 and divisor < 0) or (divisor > 0 and dividend < 0):
        return max(-quotient, -1 * 2**31)
    return min(quotient, 2**31 - 1)

# Testing
for dividend, divisor in [[10,3], [7, -3], [2**31 - 1, -1], [345345,-2], [345,345],[345,344], [-2147483648, -1]]:
    print(dividend, divisor, divide(dividend, divisor))
