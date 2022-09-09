def print_formatted(number):
    # your code goes here
    gap = len(bin(number))-2
    
    for i in range(1, number+1):
        dec = str(i).rjust(gap,' ')
        octa = str(oct(i)[2:]).rjust(gap,' ')
        hexa = str(hex(i)[2:]).rjust(gap,' ')
        bina = str(bin(i)[2:]).rjust(gap,' ')
        
        hexa = hexa.upper()
        print(dec, octa, hexa, bina)
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)