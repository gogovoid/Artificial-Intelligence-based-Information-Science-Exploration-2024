# ISHS CAFFE
# Americano 1500, Latte 2500
def select_menu(index):
    """
    display menu, calculate total price and count quantity
    :param index: index of list
    :return: None
    """
    global total_price
    print(f"You ordered {beverage[index]}. The price is {prices[index]} won.")
    total_price = total_price + prices[index]
    quantity[index] = quantity[index] + 1


beverage_price_quantity = {
    "americano coffee": [1500, 0],  # key: [price, quantity]
    "caffe latte": [2500, 0],
    "iced tea": [2300, 0]
}
total_price = 0

menu_lists = ''
#for m in range(len(beverage)):
i = 1
for k, v in beverage_price_quantity.items():
    menu_lists = menu_lists + f"{i}) {k} {v[0]}won  "
    i = i + 1
menu_lists = menu_lists + f"{i}) End order : "

while True:
    menu = input(menu_lists)
    if menu == '4':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        select_menu(0)
    elif menu == '2':
        select_menu(1)
    elif menu == '3':
        select_menu(2)
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")

for i in range(len(beverage)):
    if quantity[i] != 0:
        print(f"{beverage[i]}\n\t{prices[i]}\tx{quantity[i]}\t{prices[i] * quantity[i]}")

print(f"The total amount is {total_price} won.")
