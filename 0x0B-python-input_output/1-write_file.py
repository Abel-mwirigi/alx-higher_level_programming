#!/usr/bin/python3
"""A text writing function into a file"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file overwrites
        existing text or creates a new file
    Args:
    filename: specified name to be written into
    text: the text to be written
    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
