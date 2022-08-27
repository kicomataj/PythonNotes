"""Module to learn about Python data structures"""


"""
Primitive Data Structures

list
    - [1, 2, 3]  SQUARE BRACKETS
    - iterable
    - indexable
    - ordered
    - mutable

tuple
    - (1, 2, 3)  PARENTHESIS
    - iterable
    - indexable
    - ordered
    - immutable

set
    - {1, 2, 3}  CURLY BRACKETS
    - iterable
    - NOT INDEXABLE
    - NOT ORDERED
    - immutable
    - UNIQUE = CANNOT CONTAIN DUPLICATES

dict
    - {"key": "value"}  CURLY BRACKETS
    - iterable
    - NOT INDEXABLE (but you can perform lookups)
    - ordered
    - mutable

"""


def learn_lists():
    """Function to showcase the functionality of a list"""

    # counter = 0
    nums = [1, 2, 3, 4, 5]
    for num in nums:
        # counter += 1  # this gets called 3 times
        # print(counter)
        # print(num * num)  # finds square
        print(num ** 3)


def main():
    """Runs the main process"""

    learn_lists()


if __name__ == "__main__":
    main()
