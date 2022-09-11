# string = input()
# string = string.split(" ")
# string = list(string)
# print(f"List version: {string}")

# string = set(string)
# print(f"set version: {string}")

# string = list(string)
# print("".join(string))

from textwrap import wrap

def merge_the_tools(string, k):
    if len(string)%k == 0:
        strlst = wrap(string, k)
        for i in strlst:
            sett = set(i)
            print("".join(sett))
    else:
        print("Make sure that value of k is multiple of the string length.")

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)