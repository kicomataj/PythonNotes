

def exponential(number, power, silent=False, **kwargs):
    result = number ** power
    if kwargs.get("verbose"):
        print(result, "VERBOSE")
    elif silent:
        pass
    else:
        print(result)


def main():
    exponential(5, 3)
    exponential(5, 3, silent=True)
    exponential(5, 3, verbose=True)
    exponential(5, 3, silent=True, verbose=True)


if __name__ == "__main__":
    main()
