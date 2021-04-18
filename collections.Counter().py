from collections import Counter

shoes = int(input())
shoes_val = list(map(int, input().split()))
customers = int(input())
new_list = []
cost=0
for i in range(customers):
    shoe_price = []
    shoe,price = list(map(int,input().split()))
    shoe_price.append(shoe)
    shoe_price.append(price)
    new_list.append(shoe_price)


for i in range(len(new_list)):
    if new_list[i][0] in shoes_val:
        cost+=new_list[i][1]
        shoes_val.remove(new_list[i][0])
print(cost)
