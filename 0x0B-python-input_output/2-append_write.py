#!/usr/bin/python3
"""A text appending function"""


def append_write(filename="", text=""):
    """This function appends text to an existing file
            or creates a file if not present
    Args:
            filename: file text to be appended to
            text: text to be appended
    Returns:
            Number of characters that were appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
