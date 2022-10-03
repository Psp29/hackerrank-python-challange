# Your task is to sort the string S in the following manner:
#     # All sorted lowercase letters are ahead of uppercase letters.
#     # All sorted uppercase letters are ahead of digits.
#     # All sorted odd digits are ahead of sorted even digits.



def ginortS(S):
    if S.isalpha() & S.islower():
        priority = 0
    elif S.isalpha() & S.isupper():
        priority = 1
    elif S.isdigit() & int(S)%2 == 1:
        priority = 2
    else:
        priority = 3
    return priority, S

print(''.join(sorted(list(input()), key = ginortS, reverse= False)))    # key is Optional. A Function to execute to decide the order. Default is None