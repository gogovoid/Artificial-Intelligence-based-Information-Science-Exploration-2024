# ISHS CAFFE
# Americano 1500, Latte 2500

beverage = ["Americano", "Latte"]
prices = [1500, 2500]

while True:
    menu = int(input("1) Americano   2) Latte    3) End order : "))
    if menu == 3:
        print("Exit program..")
        break
    elif menu == 1:
        print("You ordered americano coffee. The price is 1500 won.")
    elif menu == 2:
        print("You ordered a cafe latte. The price is 2500 won.")
    else:
        print(f"Menu number {menu} you ordered does not exist. Please choose from the menu.")