import string
def print_rangoli(size):
    alphabets = string.ascii_lowercase
    
    l = []
    for i in range(n):
        s = "-".join(alphabets[i:n])
        l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
    print('\n'.join(l[:0:-1]+l))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)