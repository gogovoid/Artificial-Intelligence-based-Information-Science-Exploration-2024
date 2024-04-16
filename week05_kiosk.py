# ISHS CAFFE
# Americano 1500, Latte 2500

beverage = ["americano coffee", "caffe latte", "iced tea"]
prices = [1500, 2500, 2300]
quantity = [0, 0, 0]
total_price = 0

menu_lists = ''
for m in range(len(beverage)):
    menu_lists = menu_lists + f"{m+1}) {beverage[m]} {prices[m]}won  "
menu_lists = menu_lists + f"{len(beverage)+1}) End order : "

while True:
    menu = input(menu_lists)
    if menu == '4':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        print(f"You ordered {beverage[0]}. The price is {prices[0]} won.")
        total_price = total_price + prices[0]
        quantity[0] = quantity[0] + 1
    elif menu == '2':
        print(f"You ordered {beverage[1]}. The price is {prices[1]} won.")
        total_price = total_price + prices[1]
        quantity[1] = quantity[1] + 1
    elif menu == '3':
        print(f"You ordered {beverage[2]}. The price is {prices[2]} won.")
        total_price = total_price + prices[2]
        quantity[2] = quantity[2] + 1
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")

for i in range(len(beverage)):
    if quantity[i] != 0:
        print(f"{beverage[i]}\n\t{prices[i]}\tx{quantity[i]}\t{prices[i] * quantity[i]}")

print(f"The total amount is {total_price} won.")
