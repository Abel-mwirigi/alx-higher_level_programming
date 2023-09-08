#!/usr/bin/python3
"""An indentation program according to specific characters"""


def text_indentation(text):
    """Indents a paragraph

    Args:
    text - a string

    the paragraph indents by two lines whenever ('.' or '?' or ':') is found
    Raises:
    TypeError: if the text is not a string"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i])
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
        else:
            print(text[i], end="")
            i += 1
