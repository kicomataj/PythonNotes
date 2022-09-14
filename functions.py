"""Module for explaining Python functions"""


def function(x: int, y: int, *args, key1=None, **kwargs):
    """Function to show positional and keyword arguments"""

    # print(args[0], args[2])
    # print(f"args = {args}")
    # print(type(kwargs))
    # print(f"kwargs = {kwargs}")
    print(f"x = {x}, y = {y}")
    print(f"args = {args}")
    print(f"key1 = {key1}")
    print(f"kwargs = {kwargs}")


def main():
    """Executes the main process"""

    # function(1, 2, 3, 4, 5)  # arbitrary positional arguments
    # function(key1=20, key2=30, key3=40)  # arbitrary keyword arguments
    # function(11, 22, 33, 44, 55, key1="one", key2="two", key3="three")
    numbers = (1, 2, 3, 4, 5)
    keyring = {"key3": 44, "key1": 77, "key2": 22}
    # print(numbers, keyring)
    # function(*numbers)
    # function(1, 2, 3, 4, 5)
    function(*numbers, **keyring)
    # function(1, 2, 3, 4, 5, key3=44, key1=77, key2=22)


if __name__ == "__main__":
    main()
