def reverse_string(input_string):
    """
    Reverses the characters in the input string.

    Args:
        input_string (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Example:
        >>> reverse_string("Hello, world!")
        '!dlrow ,olleH'
    """
    result = input_string[::-1]
    return result
