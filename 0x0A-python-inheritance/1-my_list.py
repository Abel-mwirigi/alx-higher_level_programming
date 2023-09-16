#!/usr/bin/python3
"""function of a class MyList that inherits from list"""


class MyList(list):
    """class Mylist """

    
    def print_sorted(self):
        """
        prints the list in ascending order
        """
        sorted_list = sorted(self)
        print(sorted_list)
