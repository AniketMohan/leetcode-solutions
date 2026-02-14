lookup_string_to_integer = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '0':0,
}

lookup_integer_to_string = {
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    0:'0',
}

def string_to_integer(num: str) -> int:
    result = 0
    exponent = len(num)
    for digit in num:
        exponent -= 1
        result += lookup_string_to_integer[digit] * 10 ** exponent
    return result

def integer_to_string(num: int) -> str:
    if not num:
        return "0"
    result = ''

    while num:
        digit = num % 10
        result = lookup_integer_to_string[digit] + result
        num //= 10

    return result

def multiply(num1: str, num2: str) -> str:
    return integer_to_string(string_to_integer(num1) * string_to_integer(num2))

# Testing
for num1, num2 in [["2","3"], ["123","456"]]:
    print(num1, num2, multiply(num1,num2))
