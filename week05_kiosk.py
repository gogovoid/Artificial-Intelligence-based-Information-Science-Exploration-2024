# ISHS CAFFE
# Americano 1500, Latte 2500

beverage = ["Americano", "Latte", "Iced tea"]
prices = [1500, 2500, 2300]
quantity = [0, 0, 0]
total_price = 0

while True:
    menu = input("1) Americano  2) Latte   3) Iced tea   4) End order : ")
    if menu == '4':
        print("Your order has been accepted.")
        break
    elif menu == '1':
        print("You ordered americano coffee. The price is 1500 won.")
        total_price = total_price + prices[0]
        quantity[0] = quantity[0] + 1
    elif menu == '2':
        print("You ordered a cafe latte. The price is 2500 won.")
        total_price = total_price + prices[1]
        quantity[1] = quantity[1] + 1
    elif menu == '3':
        print("You ordered a iced tea. The price is 2300 won.")
        total_price = total_price + prices[2]
        quantity[2] = quantity[2] + 1
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")

for i in range(len(beverage)):
    if quantity[i] != 0:
        print(f"{beverage[i]}\n\t{prices[i]}\tx{quantity[i]}\t{prices[i] * quantity[i]}")

print(f"The total amount is {total_price} won.")
