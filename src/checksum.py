def modulo11_checksum(isbn_number: str):

    digits = ''
    for char in isbn_number:
        if char.isdigit():
            digits += char

    check_digit = digits[-1]

    total = 0
    for i in range(len(digits) - 1):
        weight = 10
        digit = digits[i]
        total += digit * weight

    checksum = total + check_digit
    return checksum % 11 == 0


number = str(input())

while number != -1:
    result = "correct" if modulo11_checksum(number) == 1 else "incorrect"
    print(result)

    number = str(input())