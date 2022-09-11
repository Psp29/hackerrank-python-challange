def split_and_join(line):
    line = line.split(" ")  # it will yeild result as ['this' 'is' 'a' 'string'] 
    line = "-".join(line)   # it will replace " " (space) with "-" and join the list into one string.
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)