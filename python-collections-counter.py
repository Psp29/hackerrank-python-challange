# Task

# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.


from collections import Counter

shoesStock = int(input("Enter total shoes in stock: ").strip())
shoesList = Counter(map(int, input("Enter available shoes sizes: ").split()))

customers = int(input("Enter total number of customers: ").strip())

income = 0

for _ in range(customers):
    size, price = map(int, input("Enter the size and price: ").split())
    if shoesList[size]:
        income += price
        shoesList[size] -= 1
print(f"Total income is: {income}.")