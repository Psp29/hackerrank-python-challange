from collections import Counter

n = int(input().strip())
string_list = Counter(input() for _ in range(n))

# print(string_list)

print(len(string_list))        
print(*string_list.values())
