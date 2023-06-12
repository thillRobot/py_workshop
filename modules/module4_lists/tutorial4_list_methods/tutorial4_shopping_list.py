# ENGR1220-001-GSET-Summer2023
# Tristan Hill, June 09, 2023
# Tutorial4 - Shopping List

items=['motor', 'wheels', 'lidar', 'pc']
prices=[200.0, 1200.01, 1200.01, 1200.01]

x=input("type a new item: ")
y=input("type the price of the new item: ")

items.append(x)
prices.append(float(y))

max_price=max(prices)
max_index=prices.index(max_price)

total_price=sum(prices)
average_price=sum(prices)/len(prices)

print(items)
print(prices)

print(max_price)
print(max_index)

print(total_price)
print(round(average_price,4))


#print(f'The average is {average_price:.3f}')