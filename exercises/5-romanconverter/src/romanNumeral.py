def jn(number: int) -> str:

    if not (0 < number < 1001):
        return "Nombre hors de portée (1-1001)"


    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    result = []
    temp_num = number

    for value, symbol in roman_map:
        while temp_num >= value:
            result.append(symbol)
            temp_num -= value

    return "".join(result)

def chiffres(number: str) -> int:

    chiffre_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]

    total = 0
    i = 0

    while i < len(number):
        for value, roman_symbol in chiffre_map:
            if number[i:i + len(roman_symbol)] == roman_symbol:
                total += value
                i += len(roman_symbol)
                break
    return total










