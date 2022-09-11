def swap_case(s):
    string = ""
    for i in s:
        if i.isupper():
            string = string + i.lower()
        elif i.islower():
            string = string + i.upper()
        else:
            string = string + i
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)