import re

def valid_palindrome(word):
    """
    Checks if a word is a valid palindrome or not

    Args:
        input_string (str): The string to be checked.

    Returns:
        bool: The result of the verification

    Example:
        >>> valid_palindrome("level")
        True
    """

    # Create pattern
    regex = re.compile('[^a-zA-Z]')

    word_without_non_alphabetic = regex.sub('', word)
    reversed_word = word_without_non_alphabetic[::-1]
    return word_without_non_alphabetic.lower() == reversed_word.lower()
