def split_and_join(line):
    # write your code here
    nl = line.split(" ")
    return "-".join(nl)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)