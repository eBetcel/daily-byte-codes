def correct_capitalization(input_string):
    """
    Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

    Args:
        input_string (str): The string to be checked

    Returns: 
        bool: the result if the string has correct capitalization

    Example:
        >>> correct_capitalization("USA")
        True
        >>> correct_capitalization("Universal")
        True
        >>> correct_capitalization("pLane")
        False
    """
    if input_string[0].isupper():
        if input_string[1:].isupper() or input_string[1:].islower():
            return True
        else:
            return False
        
    else:
        if input_string[1:].islower():
            return True
        else:
            return False
    
