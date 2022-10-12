from collections import OrderedDict as od

n = int(input().strip())
items = od()
for _ in range(n):
    *name, price = tuple(map(str, input().split()))   
    name, price = " ".join(name), int(price)
    
    if name in items:
        items[name] += price
    else:
        items[name] = price
        
for x, y in items.items():
    print(x,y)