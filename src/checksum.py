def modulo11_checksum(isbn_number: str):
    digits = ''
    for char in isbn_number:
        if char.isdigit():
            digits += char

    if len(digits) != 10: 
        raise ValueError('ISBN must have exactly 10 characters')
    
    int_digits = [int(x) for x in digits[:-1]]

    check_digit = int(digits[-1])

    total = 0
    weight = 10
    for i in int_digits:
        total += i * weight
        weight -= 1

    checksum = total + check_digit
    return checksum % 11 == 0
