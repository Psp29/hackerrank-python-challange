# Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: 2^31-1(c++ int) or 2^63-1(C++ long long int). 

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
d = int(input("Enter value of d: "))

print(f"a^b+c^d= {a**b+c**d}")