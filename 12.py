# 1 <= num <= 3999``

def intToRoman(num: int) -> str:
    result = ""
    thousands_digit = num // 1000
    hundreds_digit = num // 100 % 10
    tens_digit = num // 10 % 10
    unit_digit = num % 10

    if thousands_digit:
        if thousands_digit == 1:
            result += "M"
        if thousands_digit == 2:
            result += "MM"
        if thousands_digit == 3:
            result += "MMM"

    if hundreds_digit:
        if hundreds_digit == 1:
            result += "C"
        if hundreds_digit == 2:
            result += "CC"
        if hundreds_digit == 3:
            result += "CCC"
        if hundreds_digit == 4:
            result += "CD"
        if hundreds_digit == 5:
            result += "D"
        if hundreds_digit == 6:
            result += "DC"
        if hundreds_digit == 7:
            result += "DCC"
        if hundreds_digit == 8:
            result += "DCCC"
        if hundreds_digit == 9:
            result += "CM"

    if tens_digit:
        if tens_digit == 1:
            result += "X"
        if tens_digit == 2:
            result += "XX"
        if tens_digit == 3:
            result += "XXX"
        if tens_digit == 4:
            result += "XL"
        if tens_digit == 5:
            result += "L"
        if tens_digit == 6:
            result += "LX"
        if tens_digit == 7:
            result += "LXX"
        if tens_digit == 8:
            result += "LXXX"
        if tens_digit == 9:
            result += "XC"

    if unit_digit == 1:
        result += "I"
    if unit_digit == 2:
        result += "II"
    if unit_digit == 3:
        result += "III"
    if unit_digit == 4:
        result += "IV"
    if unit_digit == 5:
        result += "V"
    if unit_digit == 6:
        result += "VI"
    if unit_digit == 7:
        result += "VII"
    if unit_digit == 8:
        result += "VIII"
    if unit_digit == 9:
        result += "IX"

    return result

# Testing
for num in [3749, 58, 1994]:
    print(num,intToRoman(num))
