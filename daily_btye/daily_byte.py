def sum_bytes(number_1, number_2):
    """
    Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).

    Args:
        number_1 (str): String of a number in binary
        number_2 (str): String of a number in binary
    Returns:
        result (str): Sum of the number_1 and number_2

    Examples:
        >>> sum_bytes("100", "1")
        '101'
    
        >>> sum_bytes("11", "1")
        '100'

        >>> sum_bytes("1", "0")
        '1'
    """

    length = max(len(number_1), len(number_2))
    bin_number_1 = number_1.zfill(length)
    bin_number_2 = number_2.zfill(length)

    carry = 0
    result = []


    for digit1, digit2 in zip(reversed(bin_number_1), reversed(bin_number_2)):
        num1 = int(digit1)
        num2 = int(digit2)

        digit_sum = num1 + num2 + carry
        result.append(str(digit_sum % 2))

        carry = digit_sum // 2

    if carry != 0:
        result.append(str(1))
    return ''.join(reversed(result))
