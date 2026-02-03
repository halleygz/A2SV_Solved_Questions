def swap_case(s):
    swapped = ""
    for i in s:
        if i.isupper():
            swapped += i.lower()
        else:
            swapped += i.upper()
    return swapped


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
