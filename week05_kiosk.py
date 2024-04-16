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
